'''
There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire timeToLive seconds after the currentTime. If the token is renewed, the expiry time will be extended to expire timeToLive seconds after the (potentially different) currentTime.

Implement the AuthenticationManager class:

AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.
Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.
'''

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}
    
    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens.keys():
            self.tokens[tokenId] = self.timeToLive + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens.keys():
            return None
        else:
            if self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = currentTime + self.timeToLive
            else:
                return None

    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter = 0
        for key in self.tokens.keys():
            if self.tokens[key] > currentTime:
                counter += 1
        return counter
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
