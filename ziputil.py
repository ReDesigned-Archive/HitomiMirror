import os
import zipstream
from io import StringIO
from fastapi.responses import StreamingResponse

def zipfiles(path) -> StreamingResponse:
    zip_subdir = "archive"
    zip_filename = "%s.zip" % zip_subdir
    zf = zipstream.ZipFile(mode='w', compression=zipstream.ZIP_DEFLATED)
    for root, directories, files in os.walk(path):
        for filename in files:
            path1 = os.path.join(root, filename)
            zf.write(path1, path1)
    resp = StreamingResponse(zf.__iter__(), media_type="application/zip")
    resp.headers['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp