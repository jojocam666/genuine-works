
# code for a p2p network implementation and initialization



import socket
import rsa
from threading import Thread
from time import sleep
import datetime

class Peer():
  def __init__( self, maxpeers, serverport, myid=None, serverhost = None ):
	self.debug = 0

	self.maxpeers = int(maxpeers)
	self.serverport = int(serverport)

        # If not supplied, the host name/IP address will be determined
	# by attempting to connect to an Internet host like Google.
	if serverhost: self.serverhost = serverhost
	else: self.__initserverhost()

        # If not supplied, the peer id will be composed of the host address
        # and port number
	if myid: self.myid = myid
	else: self.myid = '%s:%d' % (self.serverhost, self.serverport)

        # list (dictionary/hash table) of known peers
	self.peers = {}  

        # used to stop the main loop
	self.shutdown = False  

	self.handlers = {}
	self.router = None
    # end constructor
    
  
  def makeserversocket( self, port, backlog=5 ):
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) #address family of Ipv4 type  for AF_INET and protocol type = TCP for SOCK_STREAM
	s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 ) 
	s.bind( ( '', port ) ) #Binding the listening socket to a port
	s.listen( backlog ) #Listening socket
	return s

 s = self.makeserversocket( self.serverport )
  
  while 1:
     clientsock, clientaddr = s.accept() #Accept a connection from the client
  
     t = threading.Thread( target = self.__handlepeer, args = [ clientsock ] )
     t.start()
      
      
  def mainloop( self ):
	s = self.makeserversocket( self.serverport )
	s.settimeout(2)
	self.__debug( 'Server started: %s (%s:%d)'
		      % ( self.myid, self.serverhost, self.serverport ) )

	while not self.shutdown:
	    try:
		self.__debug( 'Listening for connections...' )
		clientsock, clientaddr = s.accept()
		clientsock.settimeout(None)

		t = threading.Thread( target = self.__handlepeer, args = [ clientsock ] )
		t.start()
	    except KeyboardInterrupt:
		self.shutdown = True
		continue
	    except:
		if self.debug:
		    traceback.print_exc()
		    continue
	# end while loop

	self.__debug( 'Main loop exiting' )
	s.close()
    # end mainloop method 
    
    
  def __handlepeer( self, clientsock ):
	self.__debug( 'Connected ' + str(clientsock.getpeername()) )

	host, port = clientsock.getpeername()
	peerconn = BTPeerConnection( None, host, port, clientsock, debug=False )
	
	try:
	    msgtype, msgdata = peerconn.recvdata()
	    if msgtype: msgtype = msgtype.upper()
	    if msgtype not in self.handlers:
		self.__debug( 'Not handled: %s: %s' % (msgtype, msgdata) )
	    else:
		self.__debug( 'Handling peer msg: %s: %s' % (msgtype, msgdata) )
		self.handlers[ msgtype ]( peerconn, msgdata )
	except KeyboardInterrupt:
	    raise
	except:
	    if self.debug:
		traceback.print_exc()
	
	self.__debug( 'Disconnecting ' + str(clientsock.getpeername()) )
	peerconn.close()

    # end handlepeer method  
    
 def sendtopeer( self, peerid, msgtype, msgdata, waitreply=True ):
	if self.router:
	    nextpid, host, port = self.router( peerid )
	if not self.router or not nextpid:
	    self.__debug( 'Unable to route %s to %s' % (msgtype, peerid) )
	    return None
	return self.connectandsend( host, port, msgtype, msgdata, pid=nextpid,
				    waitreply=waitreply )

    # end sendtopeer method
  
def connectandsend( self, host, port, msgtype, msgdata, pid=None, waitreply=True ):
	msgreply = []   # list of replies
	try:
	    peerconn = BTPeerConnection( pid, host, port, debug=self.debug )
	    data = [msgtype, msgdata]
	    peerconn.sendall(data.encode())
	    self.__debug( 'Sent %s: %s' % (pid, msgtype) )
	    
	    if waitreply:
		onereply = peerconn.recv(1024)
		nonedata = [None,None]
		while (onereply != (nonedata)):
		    msgreply.append( onereply )
		    self.__debug( 'Got reply %s: %s' % ( pid, str(msgreply) ) )
		    onereply = peerconn.recv(1024)
	    peerconn.close()
	except KeyboardInterrupt:
	    raise
	except:
	    if self.debug:
		traceback.print_exc()
	
	return msgreply

    # end connectsend method
	
	
	
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((serverhost, serverport)) 
    s.sendall(msgdata) 
    onereply = s.recv(1024) 
    print(onereply)
	

	
#def recvall(self,data)
#data = b'' 
#while True: 
   #d = conn.recv(buff_size) 
   #if not d or len(d) < buff_size: 
    #  break 
   #data += d
	#return data
	
	
class Bipm():
	"""
	Class to define and use stealthy message types on the network, such as transaction or block requests
	:param bipm_type :specify if the bipm is a bipm_tx or bipm_blc
	:type bipm_type : bool
	"""
	import transactions
	import blocks
	self.bipm_types = ["bipm_tx", "bipm_blc"]
	
	def get_request_type(self,request_type):
		if new_transaction() = 1:
			request_type = "new_transaction"
		elif new_block() = 1:
			request_type = "new_block"
			return request_type
	
	def get_bipm_type(self,request_type):	
	
		if request_type = "new_transaction" :
	   		bipm_type = bipm_types[0]
		elif request_type = "new_block" :
	   		bipm_type = bipm_types[1]
	   	if not bipm_types[0] or not bipm_types[1]:
			return None
		return bipm_type
	
	def send_bipm_to_peer(self,bipm_type,msg):
		"""
		Send a specified type of bipm with its content to a random peer on the network
		:param msg: the bipm,type and content,which are to send
		:type msg: str
		"""
