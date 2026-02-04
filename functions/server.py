import sys
import os

# Add your app directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from mangum import Mangum
from crop import app

handler = Mangum(app)