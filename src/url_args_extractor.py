class UrlArgsExtractor:
    def __init__(self, url):
        if self.isUrlValid(url):
            self.url = url
        else:
         raise LookupError("Invalid URL")

    @staticmethod
    def isUrlValid(url):
        if url:
            return True
        else:
            return False

    def extractArgs(self):
        src_word = "src=" 
        dest_word = "dest="
        value_word = "value="

        src_index_start = self.findCurrencyIdx(src_word)
        src_index_end = self.url.find(dest_word) - 1

        dest_index_start = self.findCurrencyIdx(dest_word)
        dest_index_end = self.url.find(value_word) - 1
        
        src = self.url[src_index_start:src_index_end]
        dest = self.url[dest_index_start:dest_index_end]

        return src, dest

    # return start index of currency
    def findCurrencyIdx(self, currency):
        return self.url.find(currency) + len(currency)
