from datetime import datetime, timezone
from flask import Blueprint, request
from app import db
from app.models import Visit

main_bp = Blueprint("main", __name__)


@main_bp.route("/hello", methods=["GET"])
def hello():
    current_time = datetime.now(timezone.utc)

    ip = request.headers.get("X-Forwarded-For", request.remote_addr) or "unknown"

    visit = Visit(timestamp=current_time, ip_address=ip)
    db.session.add(visit)
    db.session.commit()

    return "Hello", 200