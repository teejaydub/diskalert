from DiskAlert.settings import settings
from DiskAlert.detect import check_usage

def main():
    """The main function"""
    print("Disk Check Started...")

    b = settings()
    check_usage(b.devices, b.threshold)

    print("Disk Check ended...")

if __name__ == '__main__':
    main()
