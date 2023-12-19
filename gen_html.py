part_1_html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.1.9/p5.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.topology.min.js"></script>
    <div id="vanta-canvas" style="top: 0; left: 0; width: 100%; height: 100%; position: fixed; margin: 0; z-index: -5" width="1296" height="1103"></div>
    <script>
        VANTA.TOPOLOGY({
        el: "#vanta-canvas",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 0.30,
        scaleMobile: 1.00,
        color: 0x1e52fc,
        backgroundColor: 0x0
        })
    </script>
    <style>
        body {
            background-color: black;
            color: white;
        }

        .container {
            max-width: 600px;
            margin: auto;
        }

        .server-list {
            list-style: none;
            padding: 0;
        }

        .server-item {
            border: 1px solid #ffffff;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .server-name {
            font-weight: bold;
        }

        .btn-choose {
            margin-top: 10px;
            margin-bottom: 10px;
            /* button colors; */
            background-color: rgb(29, 37, 66);
            border-color: #151c33;

        }
        .credits {
        position: fixed;
        left: 5px;
        bottom: 5px;
        color: #ffffff27;
        }   
        .hidden {
            display: none;
        }
        
    </style>
    <title>Server Choice</title>
</head>
<body>

<div class="container mt-5">
    
    <h1 class="mb-4">Choose a Server</h1>
    <ul class="server-list">"""

    

        
part_2_html = """
</ul>

    <!-- Create hidden input so Flask can get content -->
    <form id="serverForm" method="post" action="{{ url_for('handle_server') }}">
        <input type="hidden" name="server" id="serverInput" value="">
    </form>

</div>
<div class="credits">@cloudzikk   |   @b3n.j4m1n</div>
<!-- Bootstrap JS and Popper.js (required for Bootstrap components) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

<script>
    function chooseServer(serverName) {
        // Set the server input value
        document.getElementById('serverInput').value = serverName;

        // Submit the form
        document.getElementById('serverForm').submit();
    }
</script>

</body>
</html>

"""
def generate_html(names: int):
    if len(names) == 0:
        names = ["No Servers Found"]
    if len(names) > 1:
        custom_parts = []
        i = 0
        for name in names:
            try:
                name = name.replace("'", "")
            except:
                pass
            custom_part = f"""
            <!-- Server 2 -->
                    <li class="server-item">
                        <span class="server-name">{name}</span>
                        <button class="btn btn-primary btn-choose" onclick="chooseServer('{i}')">Choose</button>
                    </li>"""
            i += 1
            custom_parts.append(custom_part)
    else:
        name = names[0]
        try:
            name = name.replace("'", "")
        except:
            name = name
        custom_parts = []
        custom_part = f"""
            <!-- Server 2 -->
                    <li class="server-item">
                        <span class="server-name">{names[0]}</span>
                        <button class="btn btn-primary btn-choose" onclick="chooseServer('0')">Choose</button>
                    </li>"""
        custom_parts.append(custom_part)
    
    custom_parts = "\n".join(custom_parts)
    html = part_1_html + custom_parts + part_2_html
    with open("pages/serverlist.html", "w") as f:
        f.write(html)

