import datetime
import sys

from engine import Engine
        
# 6. Define main for assembling the above and running the program.
def main():
    engine = Engine(sys.argv)
    engine.assemble_args()

if __name__ == "__main__":
    main()
