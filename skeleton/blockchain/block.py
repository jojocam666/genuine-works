#Les transactions sont validées par lot, ce lot se nomme bloc
#La taille du bloc est fixe
#Le bloc est composé de deux éléments, un Header et un Body
#Le Header permet le bon fonctionnement de la Blockchain. Il est composé par l’Arbre de Merkle, du Hash du bloc précédent, d’un timestamp, de la version du protocole et d’un Nonce (pour le Proof-Of-Work)
#Le Body est composé uniquement de Transactions. Cas particulier, la première transaction est en direction du mineur qui a validé le bloc
