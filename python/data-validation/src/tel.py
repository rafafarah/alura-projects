import re

class Tel:
    def __init__(self, tel):
        tel = str(tel)
        if self.isvalid(tel):
            self._tel = tel
        else:
            raise ValueError("Invalid Telephone")

    def __str__(self):
        return self.format()

    def isvalid(self, tel):
        pattern = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        return True if re.findall(pattern, tel) else False

    def format(self):
        pattern = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        groups = re.search(pattern, self._tel)
        return "+{}({}){}-{}".format(groups.group(1), groups.group(2), groups.group(3), groups.group(4))
