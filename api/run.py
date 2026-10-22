
from http.server import BaseHTTPRequestHandler
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
import os
import runpy
import json
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            b"Cardiotree API is running. Use the website's Run Program button."
        )

    def do_POST(self):
        output = StringIO()
        old_cwd = os.getcwd()

        try:
            os.chdir(ROOT)

            with redirect_stdout(output), redirect_stderr(output):
                runpy.run_path(
                    os.path.join(ROOT, "main.py"),
                    run_name="__main__"
                )

            result = {
                "output": output.getvalue()
            }
            status = 200

        except Exception as exc:
            traceback.print_exc()
            result = {
                "error": f"{type(exc).__name__}: {exc}"
            }
            status = 500

        finally:
            os.chdir(old_cwd)

        body = json.dumps(result).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
