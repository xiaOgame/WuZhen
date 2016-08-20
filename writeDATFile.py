

output = open( "oneChain.dat", "w")

residueName = "P39coD100"
numAtoms = 139
numBonds = 138
numAngles = 0
numImprs = 0

output.write( "RESIDNAME %s\n" % ( residueName ))
output.write( "NUMATOM %s\n" % ( numAtoms ))
output.write( "NUMBOND %s\n" % ( numBonds ))
output.write( "NUMANGLE %s\n" % ( numAngles ))
output.write( "NUMIMPR %s\n" % ( numImprs ))

for atomIdx in range( 1, 40 ):
    output.write( "ATOM %d PDM PDM 0.0 0.0 0.0\n" % ( atomIdx ) )

for atomIdx in range( 40, 140):
    output.write( "ATOM %d CPA CPA 0.0 0.0 0.0\n" % ( atomIdx ) )

for bondIdx in range( 1, 39 ) :
    output.write( "BOND %d 0 %d %d PDM PDM \n" % ( bondIdx, bondIdx, bondIdx + 1 ))

output.write( "BOND 39 0 39 40 PDM CPA\n")

for bondIdx in range( 40, 139) :
    output.write( "BOND %d 0 %d %d CPA CPA \n" % ( bondIdx, bondIdx, bondIdx + 1 ))



