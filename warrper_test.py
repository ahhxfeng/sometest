def call_wrapper(fun):
    def wrapper(*args, **kwargs):
        print('Ready to run fun')
        res = fun(*args, **kwargs)
        print('fun run finished')
        return res
    return wrapper

@call_wrapper
def hello():
    print('hello world !!!')

@call_wrapper
def main():
    hello()

if __name__ == "__main__":
    main()
