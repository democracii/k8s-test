def find_parameter(value) :
    temp_data =[
      {
        "title_num": "3.1.1",
        "sub_info": [
          {
            "title": "1. kublet 서비스가 실행 중인지 확인",
            "status_o": "kublet 서비스를 사용 하고 있음",
            "status_x": "",
            "status_-": "kublet 서비스를 사용 중이지 않으므로 해당사항 없음"
          },
          {
            "title": "1. kubeconfig 파일의 권한이 644 이하 인지 확인",
            "status_o": "kubeconfig 파일의 권한이 644 이하로 설정 되어 있으므로 양호",
            "status_x": "kubeconfig 파일의 권한이 644 초과로 설정 되어 있으므로 양호"
          }
        ]
      },
      {
        "title_num": "3.1.2",
        "sub_info": [
          {
            "title": "1. kublet 서비스가 실행 중인지 확인",
            "status_o": "kublet 서비스를 사용 하고 있음",
            "status_x": "",
            "status_-": "kublet 서비스를 사용 중이지 않으므로 해당사항 없음"
          },                      
          {
            "title": "2. kubeconfig 파일의 소유권이 root:root로 설정되어 있는지 확인",
            "status_o": "kubeconfig 파일의 소유권이 root:root로 설정되어 있으므로 양호",
            "status_x": "kubeconfig 파일의 소유권이 root:root로 설정되어 있지 않으므로 취약"  
          }
        ]
      },
      {
        "title_num": "3.1.3",
        "sub_info": [
          {
            "title": "1. kublet 서비스가 실행 중인지 확인",
            "status_o": "kublet 서비스를 사용 하고 있음",
            "status_x": "",
            "status_-": "kublet 서비스를 사용 중이지 않으므로 해당사항 없음"
          },                      
          {
            "title": "2.kubelet-config.json 파일 사용 권한이 644이하로 설정되어 있는지 확인",
            "status_o": "kubelet-config.json 파일 사용 권한이 644이하로 설정되어 있으므로 양호",
            "status_x": "kubelet-config.json 파일 사용 권한이 644이하로 설정되어 있지 않으므로 취약"  
          }
        ]
      },
      {
        "title_num": "3.1.4",
        "sub_info": [
          {
            "title": "1. kublet 서비스가 실행 중인지 확인",
            "status_o": "kublet 서비스를 사용 하고 있음",
            "status_x": "",
            "status_-": "kublet 서비스를 사용 중이지 않으므로 해당사항 없음"
          },                      
          {
            "title": "2. kubelet-config.json 파일의 소유권이 root:root로 설정되어 있는지 확인",
            "status_o": "kubelet-config.json 파일의 소유권이 root:root로 설정되어 있으므로 양호",
            "status_x": "kubelet-config.json 파일의 소유권이 root:root로 설정되어 있지 않으므로 취약"  
          }
        ]
      },
      {
        "title_num": "3.2.1",
        "sub_info": [
          {
            "title": "1. kublet 서비스가 실행 중인지 확인",
            "status_o": "kublet 서비스를 사용 하고 있음",
            "status_x": "",
            "status_-": "kublet 서비스를 사용 중이지 않으므로 해당사항 없음"
          },                      
          {
            "title": "2. --anonymous-auth 인수가 false로 설정되어 있는지 확인",
            "status_o": "kubelet 서버에 대한 익명 요청을 허용하고 있지 않으므로 양호",
            "status_x": "kubelet 서버에 대한 익명 요청을 허용하고 있으므로 취약"  
          }
        ]
      },
       {
        "title_num": "3.2.2",
        "sub_info": [
          {
            "title": "1.--authorization-webhook 인수가 'enabled:true'로 설정되어 있는지 확인",
            "status_o": "--authorization-webhook 인수가 'enabled:true'로 설정되어 있으므로 양호",
            "status_x": "--authorization-webhook 인수가 'enabled:false'로 설정되어 있으므로 취약"
          },                      
          {
            "title": "2.--authorization-mode 인수가 AlwaysAllow로 설정되지 않았는지 확인",
            "status_o": "k--authorization-mode 인수가 AlwaysAllow로 설정되어 있지 않으므로 양호",
            "status_x": "--authorization-mode 인수가 AlwaysAllow로 설정되어 있으므로 취약"  
          }
        ]
      },
       {
        "title_num": "3.2.3",
        "sub_info": [
          {
            "title": "1. 인증서를 사용하여 Kubelet 인증을 하도록 설정되어 있는지 확인",
            "status_o": "인증서를 사용하여 Kubelet 인증을 하도록 설정하였으므로 양호",
            "status_x": "인증서를 사용하여 Kubelet 인증을 하도록 설정하지 않았으므로 취약"
          }                   
        ]
      },
       {
        "title_num": "3.2.4",
        "sub_info": [
          {
            "title": "1. readOnlyPort 비활성화 여부 확인",
            "status_o": "readOnlyPort를 비활성화하였으므로 양호",
            "status_x": "readOnlyPort를 활성화하였으므로 취약",
            "status_x_2" : "config에서 readOnlyPort를 비활성화 하지 않을 경우 기본적으로 10255/TCP로 설정되므로 취약" 
          }                   
        ]
      },
       {
        "title_num": "3.2.5",
        "sub_info": [
          {
            "title": "1. streamingConnectionIdleTimeout이 0으로 설정되어 있는지 확인",
            "status_o": "streamingConnectionIdleTimeout이 0으로 설정되어 있지 않으므로 양호",
            "status_o_2" : "streamingConnectionIdleTimeout이 0으로 설정되어 있지 않으므로 양호(기본값 : 4h0m0s)",     
            "status_x": "streamingConnectionIdleTimeout'이 0으로 설정되어 있으므로 취약"
          }                   
        ]
      },         
       {
        "title_num": "3.2.6",
        "sub_info": [
          {
            "title": "1.protectKernelDefaults 인수가 true로 설정되었는지 확인",
            "status_o": "protectKernelDefaults 인수가 true로 설정되어 있으므로 양호",
            "status_x": "protectKernelDefaults 인수가 false로 설정되어 있으므로 취약",
            "status_x_2": "protectKernelDefaults 인수가 존재하지 않으므로 취약"
          }                   
        ]
      },
       {
        "title_num": "3.2.7",
        "sub_info": [
          {
            "title": "1.makeIPTablesUtilChains 인수가 true로 설정되었는지 확인",
            "status_o": "makeIPTablesUtilChains 인수가 true로 설정되어 있으므로 양호",
            "status_x": "makeIPTablesUtilChains 인수가 false로 설정되어 있으므로 취약",
            "status_x_2": "makeIPTablesUtilChains 인수가 존재하지 않으나 Default가 true이므로 양호"
          }                   
        ]
      },
       {
        "title_num": "3.2.8",
        "sub_info": [
          {
            "title": "1.hostname-override 인수가 null로 설정되었는지 확인",
            "status_o": "hostname-override 인수가 null로 설정되어 있으므로 양호",
            "status_o_2": "hostname-override 인수가 존재하지 않으므로 양호",               
            "status_x": "hostname-override 인수를 사용하여 호스트이름을 재정의하고 있으므로 취약"
          }                   
        ]
      },
       {
        "title_num": "3.2.9",
        "sub_info": [
          {
            "title": "1.eventRecordQPS 인수가 0보다 큰 값으로 설정되었는지 확인",
            "status_o": "서비스 거부가 일어나지 않도록 이벤트 수집 속도 제한 설정을 하였으므로 양호",
            "status_o_2": "별도의 설정이 되어 있지 않아 기본값 5로 설정되므로 양호",              
            "status_x": "이벤트 수집 속도 제한을 무제한 설정으로 하여 이벤트 수집 시 서비스 거부가 일어날 수 있으므로 취약"
          }                   
        ]
      },
       {
        "title_num": "3.2.10",
        "sub_info": [
          {
            "title": "1.RotateCertificate 인수가 없거나 true로 설정되어 있는지 확인",
            "status_o": "RotateCertificate 인수가 true로 설정되어 있으므로 양호",
            "status_o_2": "RotateCertificate 인수가 존재하지 않으므로 양호",             
            "status_x": "RotateCertificate 인수가 false로 설정되어 있으므로 취약"
          }                   
        ]
      },
       {
        "title_num": "3.2.11",
        "sub_info": [
          {
            "title": "1.RotateKubeletServerCertificate 인수가 true로 설정되어 있는지 확인",
            "status_o": "RotateCertificate 인수가 true로 설정되어 있으므로 양호",
            "status_x": "RotateKubeletServerCertificate 인수가 false로 설정되어 있으므로 취약",              
            "status_x1": "RotateKubeletServerCertificate 인수가 존재하지 않으므로 취약"
          }                   
        ]
      },           
    ]

    for data in temp_data :
        if data["title_num"] == value :
            return data   

