class Solution(object):
    def defangIPaddr(self, address):
       address=address.split(".")
       return '[.]'.join(address)
