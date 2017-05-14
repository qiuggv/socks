import java.net.InetAddress;
import java.net.UnknownHostException;


public class TestDNS {

	public static void main(String[] args) throws UnknownHostException {
		System.out.println(InetAddress.getByName("www.baidu.com"));  
	}

}
