"""
$description Japanese live TV streaming website with multiple channels including news, sports, entertainment and anime.
$url abema.tv
$type live, vod
$region Japan
"""

import hashlib
import hmac
import logging
import re
import struct
import time
import uuid
from base64 import urlsafe_b64encode
from binascii import unhexlify

from requests import Response
from requests.adapters import BaseAdapter

from streamlink.exceptions import NoStreamsError
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import useragents, validate
from streamlink.stream.hls import HLSStream, HLSStreamReader, HLSStreamWriter
from streamlink.utils.crypto import AES
from streamlink.utils.url import update_qsd


log = logging.getLogger(__name__)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result


class AbemaTVHLSStreamWriter(HLSStreamWriter):
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_orig(self, segment):
        return "/tsad/" in segment.uri or super().should_filter_segment(segment)
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_1(self, segment):
        return "XX/tsad/XX" in segment.uri or super().should_filter_segment(segment)
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_2(self, segment):
        return "/TSAD/" in segment.uri or super().should_filter_segment(segment)
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_3(self, segment):
        return "/tsad/" not in segment.uri or super().should_filter_segment(segment)
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_4(self, segment):
        return "/tsad/" in segment.uri and super().should_filter_segment(segment)
    def xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_5(self, segment):
        return "/tsad/" in segment.uri or super().should_filter_segment(None)
    
    xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_1': xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_1, 
        'xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_2': xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_2, 
        'xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_3': xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_3, 
        'xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_4': xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_4, 
        'xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_5': xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_5
    }
    
    def should_filter_segment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_orig"), object.__getattribute__(self, "xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    should_filter_segment.__signature__ = _mutmut_signature(xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_orig)
    xǁAbemaTVHLSStreamWriterǁshould_filter_segment__mutmut_orig.__name__ = 'xǁAbemaTVHLSStreamWriterǁshould_filter_segment'


class AbemaTVHLSStreamReader(HLSStreamReader):
    __writer__ = AbemaTVHLSStreamWriter


class AbemaTVHLSStream(HLSStream):
    __reader__ = AbemaTVHLSStreamReader


class AbemaTVLicenseAdapter(BaseAdapter):
    """
    Handling abematv-license:// protocol to get real video key_data.
    """

    STRTABLE = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    HKEY = b"3AF0298C219469522A313570E8583005A642E73EDD58E3EA2FB7339D3DF1597E"

    _MEDIATOKEN_API = "https://api.abema.io/v1/media/token"

    _LICENSE_API = "https://license.abema.io/abematv-hls"

    _MEDIATOKEN_SCHEMA = validate.Schema({"token": str})

    _LICENSE_SCHEMA = validate.Schema({"k": str, "cid": str})

    def xǁAbemaTVLicenseAdapterǁ__init____mutmut_orig(self, session, deviceid, usertoken):
        self._session = session
        self.deviceid = deviceid
        self.usertoken = usertoken
        super().__init__()

    def xǁAbemaTVLicenseAdapterǁ__init____mutmut_1(self, session, deviceid, usertoken):
        self._session = None
        self.deviceid = deviceid
        self.usertoken = usertoken
        super().__init__()

    def xǁAbemaTVLicenseAdapterǁ__init____mutmut_2(self, session, deviceid, usertoken):
        self._session = session
        self.deviceid = None
        self.usertoken = usertoken
        super().__init__()

    def xǁAbemaTVLicenseAdapterǁ__init____mutmut_3(self, session, deviceid, usertoken):
        self._session = session
        self.deviceid = deviceid
        self.usertoken = None
        super().__init__()
    
    xǁAbemaTVLicenseAdapterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAbemaTVLicenseAdapterǁ__init____mutmut_1': xǁAbemaTVLicenseAdapterǁ__init____mutmut_1, 
        'xǁAbemaTVLicenseAdapterǁ__init____mutmut_2': xǁAbemaTVLicenseAdapterǁ__init____mutmut_2, 
        'xǁAbemaTVLicenseAdapterǁ__init____mutmut_3': xǁAbemaTVLicenseAdapterǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAbemaTVLicenseAdapterǁ__init____mutmut_orig)
    xǁAbemaTVLicenseAdapterǁ__init____mutmut_orig.__name__ = 'xǁAbemaTVLicenseAdapterǁ__init__'

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_orig(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_1(self, ticket):
        params = None
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_2(self, ticket):
        params = {
            "XXosNameXX": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_3(self, ticket):
        params = {
            "osname": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_4(self, ticket):
        params = {
            "OSNAME": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_5(self, ticket):
        params = {
            "Osname": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_6(self, ticket):
        params = {
            "osName": "XXandroidXX",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_7(self, ticket):
        params = {
            "osName": "ANDROID",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_8(self, ticket):
        params = {
            "osName": "Android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_9(self, ticket):
        params = {
            "osName": "android",
            "XXosVersionXX": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_10(self, ticket):
        params = {
            "osName": "android",
            "osversion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_11(self, ticket):
        params = {
            "osName": "android",
            "OSVERSION": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_12(self, ticket):
        params = {
            "osName": "android",
            "Osversion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_13(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "XX6.0.1XX",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_14(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "XXosLangXX": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_15(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "oslang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_16(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "OSLANG": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_17(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "Oslang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_18(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "XXja_JPXX",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_19(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_jp",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_20(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "JA_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_21(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "Ja_jp",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_22(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "XXosTimezoneXX": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_23(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "ostimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_24(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "OSTIMEZONE": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_25(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "Ostimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_26(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "XXAsia/TokyoXX",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_27(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "asia/tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_28(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "ASIA/TOKYO",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_29(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_30(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "XXappIdXX": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_31(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appid": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_32(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "APPID": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_33(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "Appid": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_34(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "XXtv.abemaXX",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_35(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "TV.ABEMA",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_36(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "Tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_37(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "XXappVersionXX": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_38(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appversion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_39(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "APPVERSION": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_40(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "Appversion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_41(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "XX3.27.1XX",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_42(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = None
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_43(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"XXAuthorizationXX": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_44(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_45(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"AUTHORIZATION": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_46(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = None
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_47(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(None, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_48(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=None, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_49(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=None)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_50(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_51(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_52(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, )
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_53(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = None
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_54(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(None, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_55(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=None)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_56(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_57(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, )
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_58(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = None

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_59(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["XXtokenXX"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_60(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["TOKEN"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_61(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["Token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_62(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = None
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_63(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(None, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_64(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params=None, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_65(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json=None)
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_66(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_67(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_68(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, )
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_69(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"XXtXX": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_70(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"T": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_71(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"T": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_72(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"XXkvXX": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_73(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"KV": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_74(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"Kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_75(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "XXaXX", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_76(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "A", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_77(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "A", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_78(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "XXltXX": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_79(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "LT": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_80(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "Lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_81(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = None
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_82(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(None, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_83(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=None)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_84(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_85(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, )
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_86(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = None
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_87(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["XXcidXX"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_88(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["CID"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_89(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["Cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_90(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = None

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_91(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["XXkXX"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_92(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["K"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_93(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["K"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_94(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = None

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_95(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(None)

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_96(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(None) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_97(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.rfind(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_98(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) / (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_99(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (59 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_100(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 * (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_101(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) + 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_102(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 2 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_103(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 + i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_104(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(None))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_105(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = None

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_106(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(None, res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_107(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", None, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_108(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, None)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_109(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_110(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_111(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, )

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_112(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack("XX>QQXX", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_113(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">qq", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_114(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">qq", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_115(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res << 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_116(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 65, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_117(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res | 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_118(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 18446744073709551616)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_119(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = None
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_120(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(None, (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_121(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), None, digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_122(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=None)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_123(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new((cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_124(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_125(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), )
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_126(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(None), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_127(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode(None), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_128(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid - self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_129(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("XXutf-8XX"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_130(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("UTF-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_131(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("Utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_132(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = None

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_133(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = None
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_134(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(None, AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_135(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, None)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_136(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(AES.MODE_ECB)
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_137(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, )
        return aes.decrypt(encvideokey)

    def xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_138(self, ticket):
        params = {
            "osName": "android",
            "osVersion": "6.0.1",
            "osLang": "ja_JP",
            "osTimezone": "Asia/Tokyo",
            "appId": "tv.abema",
            "appVersion": "3.27.1",
        }
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        res = self._session.http.get(self._MEDIATOKEN_API, params=params, headers=auth_header)
        jsonres = self._session.http.json(res, schema=self._MEDIATOKEN_SCHEMA)
        mediatoken = jsonres["token"]

        res = self._session.http.post(self._LICENSE_API, params={"t": mediatoken}, json={"kv": "a", "lt": ticket})
        jsonres = self._session.http.json(res, schema=self._LICENSE_SCHEMA)
        cid = jsonres["cid"]
        k = jsonres["k"]

        res = sum(self.STRTABLE.find(k[i]) * (58 ** (len(k) - 1 - i)) for i in range(len(k)))

        encvideokey = struct.pack(">QQ", res >> 64, res & 0xFFFFFFFFFFFFFFFF)

        # HKEY:
        # RC4KEY = unhexlify('DB98A8E7CECA3424D975280F90BD03EE')
        # RC4DATA = unhexlify(b'D4B718BBBA9CFB7D0192A58F9E2D146A'
        #                     b'FC5DB29E4352DE05FC4CF2C1005804BB')
        # rc4 = ARC4.new(RC4KEY)
        # HKEY = rc4.decrypt(RC4DATA)
        h = hmac.new(unhexlify(self.HKEY), (cid + self.deviceid).encode("utf-8"), digestmod=hashlib.sha256)
        enckey = h.digest()

        aes = AES.new(enckey, AES.MODE_ECB)
        return aes.decrypt(None)
    
    xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_1': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_1, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_2': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_2, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_3': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_3, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_4': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_4, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_5': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_5, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_6': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_6, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_7': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_7, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_8': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_8, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_9': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_9, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_10': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_10, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_11': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_11, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_12': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_12, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_13': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_13, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_14': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_14, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_15': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_15, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_16': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_16, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_17': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_17, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_18': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_18, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_19': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_19, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_20': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_20, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_21': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_21, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_22': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_22, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_23': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_23, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_24': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_24, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_25': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_25, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_26': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_26, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_27': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_27, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_28': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_28, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_29': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_29, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_30': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_30, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_31': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_31, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_32': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_32, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_33': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_33, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_34': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_34, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_35': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_35, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_36': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_36, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_37': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_37, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_38': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_38, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_39': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_39, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_40': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_40, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_41': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_41, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_42': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_42, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_43': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_43, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_44': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_44, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_45': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_45, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_46': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_46, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_47': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_47, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_48': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_48, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_49': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_49, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_50': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_50, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_51': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_51, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_52': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_52, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_53': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_53, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_54': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_54, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_55': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_55, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_56': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_56, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_57': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_57, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_58': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_58, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_59': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_59, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_60': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_60, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_61': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_61, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_62': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_62, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_63': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_63, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_64': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_64, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_65': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_65, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_66': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_66, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_67': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_67, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_68': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_68, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_69': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_69, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_70': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_70, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_71': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_71, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_72': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_72, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_73': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_73, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_74': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_74, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_75': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_75, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_76': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_76, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_77': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_77, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_78': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_78, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_79': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_79, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_80': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_80, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_81': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_81, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_82': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_82, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_83': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_83, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_84': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_84, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_85': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_85, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_86': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_86, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_87': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_87, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_88': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_88, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_89': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_89, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_90': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_90, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_91': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_91, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_92': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_92, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_93': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_93, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_94': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_94, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_95': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_95, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_96': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_96, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_97': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_97, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_98': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_98, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_99': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_99, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_100': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_100, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_101': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_101, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_102': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_102, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_103': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_103, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_104': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_104, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_105': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_105, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_106': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_106, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_107': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_107, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_108': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_108, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_109': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_109, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_110': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_110, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_111': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_111, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_112': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_112, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_113': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_113, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_114': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_114, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_115': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_115, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_116': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_116, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_117': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_117, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_118': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_118, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_119': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_119, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_120': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_120, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_121': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_121, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_122': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_122, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_123': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_123, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_124': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_124, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_125': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_125, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_126': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_126, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_127': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_127, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_128': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_128, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_129': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_129, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_130': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_130, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_131': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_131, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_132': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_132, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_133': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_133, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_134': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_134, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_135': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_135, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_136': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_136, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_137': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_137, 
        'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_138': xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_138
    }
    
    def _get_videokey_from_ticket(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_orig"), object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_videokey_from_ticket.__signature__ = _mutmut_signature(xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_orig)
    xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket__mutmut_orig.__name__ = 'xǁAbemaTVLicenseAdapterǁ_get_videokey_from_ticket'

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_orig(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_1(self, request, stream=True, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_2(self, request, stream=False, timeout=None, verify=False, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_3(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = None
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_4(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = None
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_5(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 201
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_6(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = None
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_7(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(None, request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_8(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", None)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_9(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_10(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", )[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_11(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"XXabematv-license://(.*)XX", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_12(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_13(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"ABEMATV-LICENSE://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_14(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"Abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_15(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[1]
        resp._content = self._get_videokey_from_ticket(ticket)
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_16(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = None
        return resp

    def xǁAbemaTVLicenseAdapterǁsend__mutmut_17(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        resp = Response()
        resp.status_code = 200
        ticket = re.findall(r"abematv-license://(.*)", request.url)[0]
        resp._content = self._get_videokey_from_ticket(None)
        return resp
    
    xǁAbemaTVLicenseAdapterǁsend__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAbemaTVLicenseAdapterǁsend__mutmut_1': xǁAbemaTVLicenseAdapterǁsend__mutmut_1, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_2': xǁAbemaTVLicenseAdapterǁsend__mutmut_2, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_3': xǁAbemaTVLicenseAdapterǁsend__mutmut_3, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_4': xǁAbemaTVLicenseAdapterǁsend__mutmut_4, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_5': xǁAbemaTVLicenseAdapterǁsend__mutmut_5, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_6': xǁAbemaTVLicenseAdapterǁsend__mutmut_6, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_7': xǁAbemaTVLicenseAdapterǁsend__mutmut_7, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_8': xǁAbemaTVLicenseAdapterǁsend__mutmut_8, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_9': xǁAbemaTVLicenseAdapterǁsend__mutmut_9, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_10': xǁAbemaTVLicenseAdapterǁsend__mutmut_10, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_11': xǁAbemaTVLicenseAdapterǁsend__mutmut_11, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_12': xǁAbemaTVLicenseAdapterǁsend__mutmut_12, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_13': xǁAbemaTVLicenseAdapterǁsend__mutmut_13, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_14': xǁAbemaTVLicenseAdapterǁsend__mutmut_14, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_15': xǁAbemaTVLicenseAdapterǁsend__mutmut_15, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_16': xǁAbemaTVLicenseAdapterǁsend__mutmut_16, 
        'xǁAbemaTVLicenseAdapterǁsend__mutmut_17': xǁAbemaTVLicenseAdapterǁsend__mutmut_17
    }
    
    def send(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁsend__mutmut_orig"), object.__getattribute__(self, "xǁAbemaTVLicenseAdapterǁsend__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send.__signature__ = _mutmut_signature(xǁAbemaTVLicenseAdapterǁsend__mutmut_orig)
    xǁAbemaTVLicenseAdapterǁsend__mutmut_orig.__name__ = 'xǁAbemaTVLicenseAdapterǁsend'

    def close(self):
        return


@pluginmatcher(
    name="onair",
    pattern=re.compile(r"https?://abema\.tv/now-on-air/(?P<onair>[^?]+)"),
)
@pluginmatcher(
    name="episode",
    pattern=re.compile(r"https?://abema\.tv/video/episode/(?P<episode>[^?]+)"),
)
@pluginmatcher(
    name="slots",
    pattern=re.compile(r"https?://abema\.tv/channels/.+?/slots/(?P<slots>[^?]+)"),
)
class AbemaTV(Plugin):
    _CHANNEL = "https://api.abema.io/v1/channels"

    _USER_API = "https://api.abema.io/v1/users"

    _PRGM_API = "https://api.abema.io/v1/video/programs/{0}"

    _SLOTS_API = "https://api.abema.io/v1/media/slots/{0}"

    _PRGM3U8 = "https://vod-abematv.akamaized.net/program/{0}/playlist.m3u8"

    _SLOTM3U8 = "https://vod-abematv.akamaized.net/slot/{0}/playlist.m3u8"

    SECRETKEY = (
        b"v+Gjs=25Aw5erR!J8ZuvRrCx*rGswhB&qdHd_SYerEWdU&a?3DzN9B"
        + b"Rbp5KwY4hEmcj5#fykMjJ=AuWz5GSMY-d@H7DMEh3M@9n2G552Us$$"
        + b"k9cD=3TxwWe86!x#Zyhe"
    )

    _USER_SCHEMA = validate.Schema({"profile": {"userId": str}, "token": str})

    _CHANNEL_SCHEMA = validate.Schema({
        "channels": [
            {
                "id": str,
                "name": str,
                "playback": {
                    validate.optional("dash"): str,
                    "hls": str,
                },
            },
        ],
    })

    _PRGM_SCHEMA = validate.Schema({"terms": [{validate.optional("onDemandType"): int}]})

    _SLOT_SCHEMA = validate.Schema({"slot": {"flags": {validate.optional("timeshiftFree"): bool}}})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session.http.headers.update({"User-Agent": useragents.CHROME})

    def _generate_applicationkeysecret(self, deviceid):
        deviceid = deviceid.encode("utf-8")  # for python3
        # plus 1 hour and drop minute and secs
        # for python3 : floor division
        ts_1hour = (int(time.time()) + 60 * 60) // 3600 * 3600
        time_struct = time.gmtime(ts_1hour)
        ts_1hour_str = str(ts_1hour).encode("utf-8")

        h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
        h.update(self.SECRETKEY)
        tmp = h.digest()
        for _ in range(time_struct.tm_mon):
            h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
            h.update(tmp)
            tmp = h.digest()
        h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
        h.update(urlsafe_b64encode(tmp).rstrip(b"=") + deviceid)
        tmp = h.digest()
        for _ in range(time_struct.tm_mday % 5):
            h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
            h.update(tmp)
            tmp = h.digest()

        h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
        h.update(urlsafe_b64encode(tmp).rstrip(b"=") + ts_1hour_str)
        tmp = h.digest()

        for _ in range(time_struct.tm_hour % 5):  # utc hour
            h = hmac.new(self.SECRETKEY, digestmod=hashlib.sha256)
            h.update(tmp)
            tmp = h.digest()

        return urlsafe_b64encode(tmp).rstrip(b"=").decode("utf-8")

    def _is_playable(self, vtype, vid):
        auth_header = {"Authorization": f"Bearer {self.usertoken}"}
        if vtype == "episode":
            res = self.session.http.get(self._PRGM_API.format(vid), headers=auth_header)
            jsonres = self.session.http.json(res, schema=self._PRGM_SCHEMA)
            playable = False
            for item in jsonres["terms"]:
                if item.get("onDemandType", False) == 3:
                    playable = True
            return playable
        elif vtype == "slots":
            res = self.session.http.get(self._SLOTS_API.format(vid), headers=auth_header)
            jsonres = self.session.http.json(res, schema=self._SLOT_SCHEMA)
            return jsonres["slot"]["flags"].get("timeshiftFree", False) is True

    def _get_streams(self):
        deviceid = str(uuid.uuid4())
        appkeysecret = self._generate_applicationkeysecret(deviceid)
        json_data = {"deviceId": deviceid, "applicationKeySecret": appkeysecret}
        res = self.session.http.post(self._USER_API, json=json_data)
        jsonres = self.session.http.json(res, schema=self._USER_SCHEMA)
        self.usertoken = jsonres["token"]  # for authorzation

        if self.matches["onair"]:
            onair = self.match["onair"]
            if onair == "news-global":
                self._CHANNEL = update_qsd(self._CHANNEL, {"division": "1"})
            res = self.session.http.get(self._CHANNEL)
            jsonres = self.session.http.json(res, schema=self._CHANNEL_SCHEMA)
            channels = jsonres["channels"]
            for channel in channels:
                if onair == channel["id"]:
                    break
            else:
                raise NoStreamsError
            playlisturl = channel["playback"]["hls"]
        elif self.matches["episode"]:
            episode = self.match["episode"]
            if not self._is_playable("episode", episode):
                log.error("Premium stream is not playable")
                return {}
            playlisturl = self._PRGM3U8.format(episode)
        elif self.matches["slots"]:
            slots = self.match["slots"]
            if not self._is_playable("slots", slots):
                log.error("Premium stream is not playable")
                return {}
            playlisturl = self._SLOTM3U8.format(slots)

        log.debug("URL={0}".format(playlisturl))

        # hook abematv private protocol
        self.session.http.mount("abematv-license://", AbemaTVLicenseAdapter(self.session, deviceid, self.usertoken))

        return AbemaTVHLSStream.parse_variant_playlist(self.session, playlisturl)


__plugin__ = AbemaTV
