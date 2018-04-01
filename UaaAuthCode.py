import json
import requests

class Authorization:
    #set these settings according to your application-endpoint.
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    AUTH_CODE = ""
    OAUTH_URL = ""
    #Optional, a broad helper for troubleshooting. Assign True to activate.
    VERBOSE_TROUBLESHOOTING = False    

    def troubleshootMe(self, content, text, headers):
        if "Bad Credentials" in text:
            print("TROUBLESHOOTER: I dont know, but are you sure about the authcode you are passing")
        if "client ID does not match authenticated client" in text:
            print("TROUBLESHOOTER: I dont know but, are you sure about the client_id you have provided. Either the authenticated client does not match or the client ID is wrong")
        if "The sub domain does not match to a valid identity zone" in text:
            print("TROUBLESHOOTER: I dont know but, are you sure about the ID in service-endpoint? Is the httpd://xxx-xxx-xx.somedomain.yy.yy has correct xxxs ...")
    
    def generateToken(self, Authcode, user_id):
        headers = {
            "Authorization":AuthCode,
            "Content-Type":"application/x-www-form-urlencoded"
        }
        payload = "client_id="+user_id+"&grant_type=client_credentials"
        token = ""
        expire_time = -1
        try:
            response = response.post(self.OAUTH_URL, data=payload, headers=headers)
            token = response.json().get("access_token", "Not Found")
            expire_time = response.json.get("expires_in")
            self.troubleshootMe(response.content, response.text, response.headers)
        except ConnectionError as except_ce:
            print("Token not received. Some exception occurred due to connection issues.")
            if self.VERBOSE_TROUBLESHOOTING:
                print("TROUBLESHOOTER: I dont know, but do you have some proxy issues? Try a simple 'pip install json' to verify")
        except OSError as except_os:
            print("An Exception Occurred says, OSError")
            if self.VERBOSE_TROUBLESHOOTING:
                print("TROUBLESHOOTER: I dont know but do you have any proxy issues. Try a simple 'pip install json' to verify")
        except Exception as except_ex:
            print("An Exception occurre says, Exception")
            if self.VERBOSE_TROUBLESHOOTING:
                print("TROUBLESHOOTER: I dont know but are you sure about the url? is there any oauth or token or /oauth/token to be added in the url")
            if "Bad Credentials" in text:
                print("TROUBLESHOOTER: I dont know, but are you sure about the authcode you are passing")
            if "client ID does not match authenticated client" in text:
                print("TROUBLESHOOTER: I dont know but, are you sure about the client_id you have provided. Either the authenticated client does not match or the client ID is wrong")
            if "The sub domain does not match to a valid identity zone" in text:
                print("TROUBLESHOOTER: I dont know but, are you sure about the ID in service-endpoint? Is the httpd://xxx-xxx-xx.somedomain.yy.yy has correct xxxs ...")
            pass
        except:
            print("An Exception occurred")
            pass
        return token, expire_time

    def refreshToken(self):
        return generateToken(self)