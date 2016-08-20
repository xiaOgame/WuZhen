
output = open ( "oneChain.pdb", "w" )
coordX = 0.0
coordY = 0.0
coordZ = 0.0

output.write( "HEADER ONECHAIN\n" )
for atomIdx in range( 1, 140 ):
    output.write( "HETATM %4d NONE NONE %4d %8.3f %8.3f %8.3f\n"
            % ( atomIdx, 1, coordX, coordY, coordZ + atomIdx * 1.1225) )
output.write( "END")
