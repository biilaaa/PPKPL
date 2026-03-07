import os
import ast
import re
from typing import List, Dict, Optional

class RouterVisitor(ast.NodeVisitor):
    def __init__(self):
        self.routers = {}  # name -> prefix
        self.endpoints = []  # list of dicts: {'method': str, 'endpoint': str, 'description': str}

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'router':
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'APIRouter':
                prefix = ""
                for kw in node.value.keywords:
                    if kw.arg == 'prefix':
                        if isinstance(kw.value, ast.Str):
                            prefix = kw.value.s
                        elif isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                            prefix = kw.value.value
                self.routers['router'] = prefix
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        for decorator in node.decorator_list:
            if self._is_router_decorator(decorator):
                method, path = self._extract_method_and_path(decorator)
                if method and path:
                    full_endpoint = self.routers.get('router', '') + path
                    description = self._get_description(node)
                    self.endpoints.append({
                        'method': method.upper(),
                        'endpoint': full_endpoint,
                        'description': description
                    })
        self.generic_visit(node)

    def _is_router_decorator(self, decorator):
        if isinstance(decorator, ast.Call):
            if isinstance(decorator.func, ast.Attribute):
                if isinstance(decorator.func.value, ast.Name) and decorator.func.value.id == 'router':
                    return decorator.func.attr in ['get', 'post', 'put', 'delete', 'patch']
        return False

    def _extract_method_and_path(self, decorator):
        method = decorator.func.attr.upper()
        if decorator.args:
            path_arg = decorator.args[0]
            if isinstance(path_arg, ast.Str):
                path = path_arg.s
            elif isinstance(path_arg, ast.Constant) and isinstance(path_arg.value, str):
                path = path_arg.value
            else:
                path = ""
        else:
            path = ""
        return method, path

    def _get_description(self, node):
        if ast.get_docstring(node):
            return ast.get_docstring(node).strip().split('\n')[0]  # first line
        else:
            return node.name.replace('_', ' ').title()

def scan_routers(directory: str) -> List[Dict]:
    endpoints = []
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            tree = ast.parse(content)
            visitor = RouterVisitor()
            visitor.visit(tree)
            endpoints.extend(visitor.endpoints)
    return endpoints

def write_api_docs(endpoints: List[Dict], output_file: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# API Documentation\n\n")
        f.write("| Method | Endpoint | Description |\n")
        f.write("|--------|----------|-------------|\n")
        for ep in sorted(endpoints, key=lambda x: (x['endpoint'], x['method'])):
            f.write(f"| {ep['method']} | {ep['endpoint']} | {ep['description']} |\n")

if __name__ == "__main__":
    routers_dir = os.path.join(os.path.dirname(__file__), '..', 'backend', 'app', 'routers')
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    api_file = os.path.join(docs_dir, 'API.md')
    
    endpoints = scan_routers(routers_dir)
    write_api_docs(endpoints, api_file)
    print("API documentation updated successfully!")
