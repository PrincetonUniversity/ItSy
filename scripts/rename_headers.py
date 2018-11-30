#!/usr/bin/python
import os
import argparse

def AddPrefix(fileName, prefix):
    print 'processing', fileName

    def GetUpdatedInclude(line):
        if '#include' in line and '.hpp' in line:
            targets = ['abstraction', 'ast', 'boogie', \
                        'ast/bitvec', 'ast/bool', 'ast/bvinrange', \
                        'ast/choice', 'ast/func', 'ast/hash', 'ast/mem', 'ast/node', \
                        'cExport', 'common', 'cppsimgen', \
                        'EqvChecker', 'exception', 'exportSMT', \
                        'funcReduct', \
                        'genCBMC', \
                        'horn', \
                        'imexport', \
                        'logging', \
                        'memvalues', 'MicroUnroller', \
                        'rewriter', \
                        'simplify', 'smt', 'synrewriter', 'synthesizer', \
                        'type', \
                        'Unroller', 'util', \
                        'VerilogExport'
                    ]

            terms = line.split('.')
            if 'hpp' not in terms[1]:
                print 'unknown format', line
                return line

            if '<' in line:
                headerName = terms[0].split('<')[1]
            elif '"' in line:
                headerName = terms[0].split('"')[1]
            else:
                print 'Unknwon format'

            if headerName in targets:
                newLine = '#include <' + prefix + '/' + headerName + '.hpp>\n'
                return newLine

        return line

    fileBuff = []

    with open(fileName, 'r') as rFile:
        for line in rFile:
            newLine = GetUpdatedInclude(line)
            fileBuff.append(newLine)

    
    with open(fileName, 'w') as wFile:
        for line in fileBuff:
            print >> wFile, line,
   

def AddPrefixRecursive(path, prefix):
    rootDir = path
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            filePath = os.path.join(dirName, fname)
            AddPrefix(filePath, prefix)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename include path with prefix')
    parser.add_argument('-pref', type = str, help = 'Prefix to preppend', default = 'ilang')
    parser.add_argument('-file', type = str, help = 'File name for renaming', default = '')
    parser.add_argument('-path', type = str, help = 'Path for recursive process', default = '')
    args = parser.parse_args()

    if args.pref == '':
        print 'empty prefix'
        exit(1)

    if args.path and os.path.exists(args.path):
        AddPrefixRecursive(args.path, args.pref)

    if args.file and os.path.exists(args.file):
        AddPrefix(args.file, args.pref)

