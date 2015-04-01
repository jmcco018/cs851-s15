/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import de.l3s.boilerpipe.BoilerpipeProcessingException;
import de.l3s.boilerpipe.document.TextDocument;
import de.l3s.boilerpipe.extractors.ArticleExtractor;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.FileWriter;

/**
 *
 * @author jessica
 */
public class A3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws MalformedURLException, BoilerpipeProcessingException, FileNotFoundException, IOException {
        //URL url = new URL("http://wedding.tate2.com");
        // NOTE: Use ArticleExtractor unless DefaultExtractor gives better results for you
        //String text = ArticleExtractor.INSTANCE.getText("body.html");
        BufferedReader files = new BufferedReader(new FileReader("GoodFiles"));
        String file = files.readLine();
        while (file != null) {
            BufferedReader br = new BufferedReader(new FileReader(file));
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                sb.append("\n");
                line = br.readLine();
            }
            br.close();
            String text = ArticleExtractor.INSTANCE.getText(sb.toString());
            System.out.println(text);
            String[] fileName=file.split("/");
            String outputFile="./bodyFiles/"+fileName[3]+".txt";
            PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(outputFile, true)));
            out.println(text);
            out.close();
            file = files.readLine();

            
        }
    }
    
}
