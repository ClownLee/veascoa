import random, hashlib, time, datetime, jwt
from utils.constants.index import SIGN_KEY

class Tools:
    def toJson(_self):
        names = []
        datas = []
        for f in _self._meta.fields:
           names.append(f.name)
        for attr in names:
            if attr in ['start_time', 'end_time', 'create_time', 'update_time', 'get_time', 'birthday', 'graduated_time']:
                value = getattr(_self, attr).strftime('%Y-%m-%d %H:%M:%S')
            else:
                value = getattr(_self, attr)

            datas.append((attr, value))

        return dict(datas)
        # return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

    def random(len=5):
        return (''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], len)))
    
    def md5(password, salt=''):
        if password in ['', None]:
            raise Exception('请输入明文密码')
        
        if password in ['', None]:
            raise Exception('请输入密码盐值')
        
        return hashlib.md5((str(password)+str(salt)).encode()).hexdigest()

    def sign(userinfo):
        encoded_jwt = jwt.encode({
            "exp": str((datetime.datetime.now() + datetime.timedelta(seconds=172800)).strftime('%Y-%m-%d %H:%M:%S')), # 两天后过期
            "user": dict(userinfo),
        }, SIGN_KEY, ["HS256"])

        return encoded_jwt

    def verifySign(token):
        decoded = jwt.decode(token, SIGN_KEY, ["HS256"])
        print(decoded)