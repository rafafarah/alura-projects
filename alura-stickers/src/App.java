import java.io.InputStream;
import java.net.URL;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {

        // do an http connection and get top 250 movies
        String url = "https://raw.githubusercontent.com/alura-cursos/imersao-java-2-api/main/NASA-APOD.json";
        ContentExtractor extractor = new NasaContentExtractor();
        // String url = "https://raw.githubusercontent.com/alura-cursos/imersao-java-2-api/main/TopMovies.json";
        // ContentExtractor extractor = new ImdbContentExtractor();

        ClientHttp clientHttp = new ClientHttp();
        String json = clientHttp.getData(url);

        // extract desired data (title, poster, rating)
        List<Content> contentList = extractor.extractContent(json);

        // show data
        var stickerFactory = new StickerFactory();
        for (Content content : contentList) {
            InputStream inputStream = new URL(content.getUrlImage()).openStream();
            stickerFactory.create(inputStream, "output/" + content.getTitle() + ".png");
        }
    }
}

/*
 * Challenges:
 * 1- Use different endpoits
 * 2- Improve output
 * 3- Hide API key in a configuration file
 *
 * 4- Center sticker text based on the text length
 * 5- Change font
 * 6- Add a new image and a text to the original image
 *
 * 7- Change Content class to Record
 * 8- Create custom exceptions
 * 9- Map 2 lists (lambda) with java 8
 * 10- Group url and extractor in an enum
 * 11- Use more complex API
 */