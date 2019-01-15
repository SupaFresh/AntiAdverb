import compileall
import AntiAdverb.maincode
import AntiAdverb.alpabatize_list

compileall.compile_dir('AntiAdverb/', force=True)
AntiAdverb.alpabatize_list.main()
AntiAdverb.maincode.pkg_check()
AntiAdverb.maincode.main()

