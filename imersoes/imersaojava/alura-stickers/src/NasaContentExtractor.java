import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class NasaContentExtractor implements ContentExtractor{

    public List<Content> extractContent(String json) {

        var parser = new JsonParser();
        List<Map<String, String>> listOfAttributes = parser.parse(json);
        List<Content> contentList = new ArrayList<>();

        for (Map<String, String> attibute : listOfAttributes) {
            var title = attibute.get("title").replace(": "," ");
            var urlImage = attibute.get("url");

            contentList.add(new Content(title, urlImage));
        }

        return contentList;
    }
}
