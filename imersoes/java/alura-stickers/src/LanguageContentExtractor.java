import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LanguageContentExtractor implements ContentExtractor {

    public List<Content> extractContent(String json) {

        var parser = new JsonParser();
        List<Map<String, String>> listOfAttributes = parser.parse(json);
        List<Content> contentList = new ArrayList<>();

        for (Map<String, String> attibute : listOfAttributes) {
            var languageName = attibute.get("languageName").replace(": "," ");
            var urlLanguage = attibute.get("languageUrl");

            contentList.add(new Content(languageName, urlLanguage));
        }

        return contentList;
    }
}
