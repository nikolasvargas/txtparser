from source.models import *  # noqa: F403
from typing import Dict, Any


def get_identifier(id: int) -> Dict[int, Any]:
    subclasses = [cls for cls in Identifier.__subclasses__()]
    identifiers = [classname.identifier() for classname in subclasses]
    return dict(zip(identifiers, subclasses))
