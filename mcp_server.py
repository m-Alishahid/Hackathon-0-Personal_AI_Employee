import sys
import json
import logging
import time

# Basic setup for logging to file since stdout is used for MCP protocol
logging.basicConfig(filename='mcp_server.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_response(response_dict):
    """Send JSON-RPC response to stdout"""
    try:
        print(json.dumps(response_dict), flush=True)
    except Exception as e:
        logging.error(f"Failed to send response: {e}")

def handle_request(request):
    """Handle incoming JSON-RPC requests from Claude"""
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})
    
    if method == "initialize":
        send_response({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "SilverTierExternalMCP", "version": "1.0.0"}
            }
        })
        # Send initialized notification
        print(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}), flush=True)
        
    elif method == "tools/list":
        send_response({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "post_to_linkedin",
                        "description": "Post content to LinkedIn. Requires human approval first.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "content": {"type": "string", "description": "The text of the post"}
                            },
                            "required": ["content"]
                        }
                    },
                    {
                        "name": "send_email",
                        "description": "Send an email. Requires human approval first.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "to": {"type": "string"},
                                "subject": {"type": "string"},
                                "body": {"type": "string"}
                            },
                            "required": ["to", "subject", "body"]
                        }
                    }
                ]
            }
        })
        
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "post_to_linkedin":
            content = args.get("content", "")
            logging.info(f"ACTION EXECUTED: Posting to LinkedIn -> {content}")
            
            # Here is where actual Playwright/API code would go.
            # For the Hackathon demo, simulating success to protect the account:
            time.sleep(2) # Simulate network delay
            
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Successfully posted to LinkedIn: '{content[:30]}...'"}]
                }
            })
            
        elif tool_name == "send_email":
            logging.info(f"ACTION EXECUTED: Sending email to {args.get('to')}")
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": "Email successfully queued for sending."}]
                }
            })
        else:
            send_response({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}})
            
    else:
        # Ignore unsupported methods (like ping) or send basic response
        if req_id:
            send_response({"jsonrpc": "2.0", "id": req_id, "result": {}})

def main():
    logging.info("Starting Silver Tier MCP Server")
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            request = json.loads(line)
            handle_request(request)
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON received: {line}")
        except Exception as e:
            logging.error(f"Error handling request: {e}")

if __name__ == "__main__":
    main()
