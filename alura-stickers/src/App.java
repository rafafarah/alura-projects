import java.io.InputStream;
import java.net.URI;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) throws Exception {

        // do an http connection and get top 250 movies
        String url = "https://raw.githubusercontent.com/alura-cursos/imersao-java-2-api/main/TopMovies.json";
        URI addr = URI.create(url);
        var client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(addr).GET().build();
        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        String body = response.body();

        // extract desired data (title, poster, rating)
        var parser = new JsonParser();
        List<Map<String, String>> listOfMovies = parser.parse(body);

        // show data
        var stickerFactory = new StickerFactory();
        for (Map<String,String> movie : listOfMovies) {
            InputStream inputStream = new URL(movie.get("image")).openStream();
            stickerFactory.create(inputStream, "output/" + movie.get("title") + ".png");
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
 */