from MyCapytain.resolvers.cts.local import CtsCapitainsLocalResolver
from MyCapytain.common.constants import Mimetypes
import os

os.mkdir('text')
Repository = CtsCapitainsLocalResolver(["./"])
for text in Repository.texts:
    try:
        interactive_text = Repository.getTextualNode(text.id)
        plaintext = interactive_text.export(Mimetypes.PLAINTEXT) 
        with open('text/{}.txt'.format(text.id.split(':')[-1]), mode='w') as f:
            f.write(plaintext)
    except Exception as E:
        print(E)
        continue