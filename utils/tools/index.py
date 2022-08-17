import random, hashlib
class Tools:
    def random(len=5):
        return (''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], len)))
    
    def md5(password, salt=''):
        if password in ['', None]:
            raise Exception('请输入明文密码')
        
        if password in ['', None]:
            raise Exception('请输入密码盐值')
        
        return hashlib.md5((str(password)+str(salt)).encode()).hexdigest()