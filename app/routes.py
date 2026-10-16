from datetime import datetime, timezone
from flask import Blueprint, request
from app import db
from app.models import Visit

main_bp = Blueprint("main", __name__)


@main_bp.route("/hello", methods=["GET"])
def hello():
    # 1. Получаем текущее время
    current_time = datetime.now(timezone.utc)

    # 2. Получаем IP-адрес клиента
    ip = request.headers.get("X-Forwarded-For", request.remote_addr) or "unknown"

    # 3. Сохраняем запись в таблицу Visit
    visit = Visit(timestamp=current_time, ip_address=ip)
    db.session.add(visit)
    db.session.commit()

    # 4. Возвращаем 200 OK с телом «Hello»
    return "Hello", 200