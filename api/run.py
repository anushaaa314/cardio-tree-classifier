
from contextlib import redirect_stdout, redirect_stderr
from http.server import BaseHTTPRequestHandler
from io import StringIO
import os
import runpy
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        output = StringIO()
        try:
            # main.py is run without interactive input() pauses.
            old_cwd = os.getcwd()
            os.chdir(ROOT)
            try:
                with redirect_stdout(output), redirect_stderr(output):
                    runpy.run_path(os.path.join(ROOT, "main.py"), run_name="__main__")
            finally:
                os.chdir(old_cwd)

            body = output.getvalue().encode("utf-8", errors="replace")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            import json
            self.wfile.write(json.dumps({"output": body.decode("utf-8")}).encode("utf-8"))
        except Exception as exc:
            import json
            body = json.dumps({"error": f"{type(exc).__name__}: {exc}"}).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
