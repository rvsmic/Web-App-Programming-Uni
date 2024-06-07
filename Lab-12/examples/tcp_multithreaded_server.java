class ClientThread extends Thread {

    private Socket clientSocket;

    public ClientThread(Socket client) {
        this.clientSocket = client;
    }

    @Override
    public void run() {

        try {

            // wysylanie/odbieranie danych do/od klienta

            clientSocket.close();

        } catch (IOException ex) { }
    }
}

class Server {

    private Socket client_connection = null;
    private ServerSocket server = null;
    private int port = 0;

    public Server(int port) {
        this.port = port;
    }

    public void start() {
        try {

            this.server = new ServerSocket(this.port);

            while (true) {
                
                client_connection = server.accept();

                ClientThread c = new ClientThread(client_connection);
                	
                c.start();
            }

        } catch (IOException ex) { }
    }
}

public class tcp_multithreaded_server {

    public static void main(String[] args) {
        
        Server s = new Server(6666);
        s.start();
    }  
} 
