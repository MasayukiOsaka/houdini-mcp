import hou
from .server import HoudiniMCPServer

def start_server(port=9876):
    if not hasattr(hou.session, "houdinimcp_server") or hou.session.houdinimcp_server is None:
        hou.session.houdinimcp_server = HoudiniMCPServer(port=port)
        hou.session.houdinimcp_server.start()
    else:
        print("Houdini MCP Server is already running.")

def stop_server():
    if hasattr(hou.session, "houdinimcp_server") and hou.session.houdinimcp_server:
        hou.session.houdinimcp_server.stop()
        hou.session.houdinimcp_server = None
    else:
        print("Houdini MCP Server is not running.")

# Optional auto-start
# Note: This requires Houdini GUI mode (won't work in hython/hbatch)
#
# Usage:
#     If you want the MCP server to start automatically when Houdini launches,
#     add the following to your pythonrc.py:
#
#     import houdinimcp
#     houdinimcp.initialize_plugin(port=9876)  # You can change the port number
#
def initialize_plugin(port=9876):
    # Set up default session toggles if desired
    if not hasattr(hou.session, "houdinimcp_use_assetlib"):
        hou.session.houdinimcp_use_assetlib = False
    # Auto-start server if you want:
    start_server(port)
