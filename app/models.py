from datetime import datetime, timezone
from app import db


class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    ip_address = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Visit {self.id} from {self.ip_address}>"