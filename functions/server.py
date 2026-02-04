import sys
import os

# Force add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from mangum import Mangum
from crop import app

handler = Mangum(app)

# For debugging
def lambda_handler(event, context):
    return handler(event, context)
