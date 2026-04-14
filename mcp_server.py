import json

"""
Integración MCP (Model Context Protocol).
Este script levanta herramientas pseudo-locales al sistema que Copilot usará
como un Context Server durante la ejecución. 
"""

def mcp_tool_info():
    """ Devuelve información falsa usando los specs de MCP """
    return json.dumps({
        "mcp_version": "1.0",
        "description": "Servidor de herramientas extendidas",
        "capabilities": ["read_file", "search_repo"]
    })

if __name__ == "__main__":
    print("Iniciando MCP Server en puerto local (Simulado)...")
    print(f"Info de Servidor: {mcp_tool_info()}")
