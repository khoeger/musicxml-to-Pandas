import xml.etree.ElementTree as ET
import music21 as m21
tree = ET.parse("cabs_piano_oboe_v3.xml")
root = tree.getroot()

"""
print(root.tag, root.attrib)
for child in root:
    print(child.tag, child.attrib, child.text)
"""
# -- HELPER FUNCTIONS
def listChildren(rootFindAll):
    outList = []
    for child in rootFindAll: # part list
        for i in range(len(child)):
            tag = child[i].tag
            #print(child[i].tag, child[i].attrib, child[i].text)
            if tag == 'part-group':
                pass
            else:
                attribList = child[i].attrib
                keyList = list(attribList.keys())
                for key in keyList:

                    outList.append(attribList[key])
    return(outList)

def returnMeasureInfo(partId, measureNum):
    # Query base
    specificPart = "./part[@id='"+str(partId)+"']"
    specificMeasure = specificPart+"/measure[@number='"+str(measureNum)+"']"

    # fifths <-- Sharps?
    #fifthsQuery = root.findall(specificMeasure+"/attributes/key/fifths")#.text
    #fifths = fifthsQuery[0].text

    # beats
    #beatsQuery = root.findall(specificMeasure+"/attributes/time/beats")#.text
    #beats = beatsQuery[0].text
    #beatTypeQuery = root.findall(specificMeasure+"/attributes/time/beat-type")
    #beatType = beatTypeQuery[0].text

    # tempo
    #tempoQuery = root.findall(specificMeasure+"/sound")#.text
    #tempo = tempoQuery[0].attrib['tempo']

    # note
    isRest = root.findall(specificMeasure+"/note/rest")#[0].attrib['measure']
    #print(isRest)
    if bool(isRest) == True:
        pitch = 0
        durationQuery = root.findall(specificMeasure+"/note/duration")#.text
        duration = durationQuery[0].text
    else:
        pitchStepQuery = root.findall(specificMeasure+"/note/pitch/step")#.text
        pitchStep = pitchStepQuery[0].text
        pitchOctaveQuery = root.findall(specificMeasure+"/note/pitch/octave")#.text
        pitchOctave = pitchOctaveQuery[0].text
        pitch = m21.pitch.Pitch(str(pitchStep+pitchOctave)).frequency
        durationQuery = root.findall(specificMeasure+"/note/duration")#.text
        duration = durationQuery[0].text

    #return([fifths, beats, beatType, tempo, pitch, int(duration)/12])
    return([pitch, int(duration)/12])

# Find title, author, copyright year
title = root.findall("./movement-title")[0].text
author = root.findall("./identification/creator")[0].text
copyright = root.findall("./identification/rights")[0].text

# Find part list
parts = root.findall("./part-list")
partList = listChildren(parts)
# Find 1 part, partList[0]
partId = partList[0]
specificPart = "./part[@id='"+str(partId)+"']"

# Find all measures in a part
measures = root.findall(specificPart+"/measure")
# One measure
#measureNum = measures[0].attrib['number']
size = 0
for num in range(len(measures)):
    measureNum = measures[num].attrib['number']
    measureInfo = returnMeasureInfo(partId, measureNum)
    print(measureInfo)
    size +=1
print(size)


#"""
measureNum = 1
specificMeasure = specificPart+"/measure[@number='"+str(measureNum)+"']"
#print(bool(root.findall(specificMeasure+"/note/rest")))#[0].attrib['measure'])
"""
# fifths <-- Sharps?
fifthsQuery = root.findall(specificMeasure+"/attributes/key/fifths")#.text
fifths = fifthsQuery[0].text

# beats
beatsQuery = root.findall(specificMeasure+"/attributes/time/beats")#.text
beats = beatsQuery[0].text
beatTypeQuery = root.findall(specificMeasure+"/attributes/time/beat-type")
beatType = beatTypeQuery[0].text

# tempo
tempoQuery = root.findall(specificMeasure+"/sound")#.text
tempo = tempoQuery[0].attrib['tempo']

# note
pitchStepQuery = root.findall(specificMeasure+"/note/pitch/step")#.text
pitchStep = pitchStepQuery[0].text
pitchOctaveQuery = root.findall(specificMeasure+"/note/pitch/octave")#.text
pitchOctave = pitchOctaveQuery[0].text
durationQuery = root.findall(specificMeasure+"/note/duration")#.text
duration = durationQuery[0].text
"""
# Prints
# print(title)        # title
# print(author)       # author
# print(copyright)    # copyright
# print(partList)     # part list
#print(measureList)
#print(measureNum)
#print(beats)
#print(beatType)
#print(fifths)
#print(tempo)
#print(pitchStep+pitchOctave)
#print(m21.pitch.Pitch(str(pitchStep+pitchOctave)).frequency)
#print(int(duration)/12)
