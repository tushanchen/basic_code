import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='zhangyalin_fashenjing.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
def test():
    num_list = [1,2,3,4,5]
    for num in num_list:
        try:
            print(num)
            raise Exception('zyl发神经了')
        except Exception as e:
            logging.error(e)  # 打报错日志

if __name__ == '__main__':
    test()