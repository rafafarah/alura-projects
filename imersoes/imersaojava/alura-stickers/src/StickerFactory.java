import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.InputStream;

import javax.imageio.ImageIO;

public class StickerFactory {

    public void create(InputStream inputStream, String outputFileName) throws Exception {

        // read image
        // InputStream inputStream = new FileInputStream(new File("input/movie.jpg"));
        // InputStream inputStream = new URL("https://raw.githubusercontent.com/alura-cursos/imersao-java-2-api/main/TopMovies_1.jpg").openStream();
        BufferedImage inputImage = ImageIO.read(inputStream);

        // create new image with transpatent background
        int width = inputImage.getWidth();
        int height = inputImage.getHeight();
        int newHeight = height + 200;
        BufferedImage outputImage = new BufferedImage(width, newHeight, BufferedImage.TRANSLUCENT);

        // copy original image to new file (in memory)
        Graphics2D graphics = (Graphics2D) outputImage.getGraphics();
        graphics.drawImage(inputImage, 0, 0, null);

        // configure text
        graphics.setColor(Color.ORANGE);
        graphics.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 64));

        // add text to new image
        graphics.drawString("Finally weekend", 85, newHeight - 100);

        // save new image in a file
        ImageIO.write(outputImage, "png", new File(outputFileName));
        // File myFile = new File("output/sticker.png");
        // System.out.println("Attempting to read from file in: "+myFile.getCanonicalPath());
        // ImageIO.write(outputImage, "png", myFile);
    }
}
