class UrlArgsExtractor:
    def __init__(self, url):
        if self.isUrlValid(url):
            self.url = url.lower()
        else:
         raise LookupError("Invalid URL")

    @staticmethod
    def isUrlValid(url):
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False

    def extractArgs(self):
        src_word = "src=" 
        dest_word = "dest="
        value_word = "value="

        src_index_start = self.findCurrencyIdx(src_word)
        src_index_end = self.url.find(dest_word) - 1
        src = self.url[src_index_start:src_index_end]

        if (src == dest_word[:len(dest_word)-1]):
            self.replaceSrcIfEqualDest()
            src = "brl"

        dest_index_start = self.findCurrencyIdx(dest_word)
        dest_index_end = self.url.find(value_word) - 1
        dest = self.url[dest_index_start:dest_index_end]

        return src, dest

    # return start index of currency
    def findCurrencyIdx(self, currency):
        return self.url.find(currency) + len(currency)

    def replaceSrcIfEqualDest(self):
        self.url = self.url.replace("dest", "brl", 1)
        print(self.url)

    def extractValue(self):
        value_word = "value="

        value_index_start = self.findCurrencyIdx(value_word)
        value = self.url[value_index_start:]

        return int(value)