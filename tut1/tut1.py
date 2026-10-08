import json
from http.server import BaseHTTPRequestHandler, HTTPServer

events = [{"id": "ev_101", "title": "Jazz Ensemble: Fall Concert",
     "seatsLeft": 42},
    {"id": "ev_102", "title": "Improv Night",
     "seatsLeft": 0},]

class Handler(BaseHTTPRequestHandler):

    def do_Get(self):

        #todo1

        if self.path == "____":
            self._send(200, events)
        else:
            self._send(405, {"error": "not found"})
    
    def _send(self, status, body):

        payload = json.dumps(body).encode()

        self.send_response(status)
        self.send_header("C", "json")
        self.send_header("length", str(len(payload)))
        self.end_headers()

        self.wfile.write(payload)

if __name__ == "__main__":
    HTTPServer(("",3000), Handler).serve_forever()

