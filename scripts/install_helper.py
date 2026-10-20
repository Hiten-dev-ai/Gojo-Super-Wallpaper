import subprocess
import time
import re
import xml.etree.ElementTree as ET

device = "SCU4VSEQ8HV8RG85"
apk_path = r"D:\Projects\GojoSuperWallpaper\prebuilt\GojoSuperWallpaper.apk"

print("Waking screen...")
subprocess.run(["adb", "-s", device, "shell", "input", "keyevent", "KEYCODE_WAKEUP"])

print("Starting install...")
proc = subprocess.Popen(["adb", "-s", device, "install", "-r", "-d", apk_path],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

clicked = False
for attempt in range(15):
    time.sleep(1)
    if proc.poll() is not None:
        break
    
    # Dump window hierarchy
    res = subprocess.run(["adb", "-s", device, "shell", "uiautomator", "dump", "/data/local/tmp/uidump.xml"],
                         capture_output=True, text=True, timeout=10)
    if res.returncode != 0:
        continue
    
    cat_res = subprocess.run(["adb", "-s", device, "shell", "cat", "/data/local/tmp/uidump.xml"],
                             capture_output=True, text=True, timeout=5)
    xml_data = cat_res.stdout
    if not xml_data or "<hierarchy" not in xml_data:
        continue

    # Look for button or node with text containing 'Install' or 'install' or 'OK'
    try:
        root = ET.fromstring(xml_data)
        for node in root.iter():
            text = node.attrib.get("text", "")
            resource_id = node.attrib.get("resource-id", "")
            bounds = node.attrib.get("bounds", "")
            
            # Check for install buttons
            if (any(word in text.lower() for word in ["install", "allow", "continue"]) or 
                any(id_word in resource_id.lower() for id_word in ["install", "ok", "action_button", "positive"])):
                print(f"Candidate node: text='{text}', id='{resource_id}', bounds={bounds}")
                m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", bounds)
                if m:
                    x = (int(m.group(1)) + int(m.group(3))) // 2
                    y = (int(m.group(2)) + int(m.group(4))) // 2
                    print(f"Clicking at ({x}, {y})")
                    subprocess.run(["adb", "-s", device, "shell", "input", "tap", str(x), str(y)])
                    clicked = True
    except Exception as e:
        print(f"XML parse error: {e}")

out, err = proc.communicate()
print("Install process finished.")
print("STDOUT:", out)
print("STDERR:", err)
