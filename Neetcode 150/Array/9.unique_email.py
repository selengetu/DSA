class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        uset= set()
        for email in emails:
            local, domain = email.split('@')
            if '.' in local:
                local = local.replace(".", "")
            if '+' in local:
                local=local.split('+')[0]
            uset.add((local,domain))
        return len(uset)