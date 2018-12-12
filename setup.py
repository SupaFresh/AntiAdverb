import compileall
import AntiAdverb

compileall.compile_dir('AntiAdverb/', force=True)
AntiAdverb.maincode.run()

