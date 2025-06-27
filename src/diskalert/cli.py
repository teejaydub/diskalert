from .settings import settings
from .detect import check_usage

def app():
    print("Disk Check Started...")
    b = settings()
    check_usage(b.devices, b.threshold)
    print("Disk Check ended...")

if __name__ == '__main__':
  app()
