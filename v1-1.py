o
    ,��b	  �                   @   s>  d dl mZ d dlmZ d dlmZmZmZmZ d dl	m
Z
mZmZmZ d dlmZ d dlmZmZ d dlmZmZmZ d dlZd dlZd dlZd dlZd d	lmZ d dlZd dlZd dlZd dlZd d
lmZm Z m!Z! ej"dd� d dlm"Z"mZ e"�  ej#Z$ej%Z&ej'Z(ej)Z*ej+Z,ej-Z.e&e(e*e,e.gZ/dd� Z0e0�  e1dd��Z2ee2�Z3e4e3�Z5dZ6dZ7e5e6d  e7d  Z8W d  � n1 s�w   Y  e9e8�Z:e:d a;e1dd��Z<ee<�Z3e4e3�Z5e:Z6dZ7e5e6d  e7d  Z=W d  � n1 s�w   Y  e9d�Z>e?d�Z@e=ZAe�B� ZCeC�Dd� eCd d ZEdZFdd� ZGeG�  dS )�    )�TelegramClient)�GetDialogsRequest)�InputPeerEmpty�InputPeerChannel�InputPeerUser�PeerUser)�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantError)�InviteToChannelRequest)�GetFullChannelRequest�JoinChannelRequest)�types�utils�errorsN)�reader)�Fore�Back�StyleT)Z	autoreset)�initr   c                  C   s2   dd l } t�d� tdt� dt� dt� d�� d S )Nr   �clear�
u�  

               ┏┳┳━┳┳━━┳━━┳━┳━┳━┳━━┓╋╋╋╋┏━━━┓
               ┃┃┃┃┃┣┓┏┫┏┓┃┃┃┃┃┳┻┓┓┃┏━┳━┫┏━┓┃
               ┃┃┃┃┃┃┃┃┃┣┫┃┃┃┃┃┻┳┻┛┃┗┓┃┏┻┛┏┛┃
               ┗━┻┻━┛┗┛┗┛┗┻┻━┻┻━┻━━┛╋┗━┛┏┓┗┓┃uj   
               ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┗━┛┃z

)�random�os�system�print�cy�ye�r)r   � r    �/storage/emulated/0/cre/v1-1.py�HackingZonepost   s   
���r"   �
memory.csvr   �   z	phone.csvi�$ Z 7e14b38d250953c8c1e94fd7b2d63550z
config.ini�HackingZoneZToGroup�d   c                   C   s  t } t�t�}td|� �tt�}|��  |�� s5t	t
jtj d � |�|� |�|tt
jtj d �� |�� }|js@|j}n|jd |j }d}g }t|dd��;}tj|dd	d
�}t|d � |D ]#}	i }|	d |d< |	d |d< t|	d �|d< |	d |d< |�|� qbW d   � n1 s�w   Y  tdd��}
t|
�}t|�}d}d}||d  |d  }W d   � n1 s�w   Y  t|�}|d }tdd��}
t|
�}t|�}d}d}||d  |d  }W d   � n1 s�w   Y  t|�}|d }tdddd��}tj|dd	d
�}|�t||g� W d   � n	1 �sw   Y  |D �]`}t|�t|d �k�rVt|d �t|�k�rVz7d}|d dk�rOt	d� W �q%|t| |d g�� t
jtj d }t	t
jtj  d � t!�"t#�$dd�� W n� t%�y�   t
jtj d }t!�"t#�$dd�� Y n� t&�y�   d }Y n~ t'�y� } zd!}t	t
jtj  d" � t!�"t#�$d#d$�� W Y d }~n[d }~w t(�y� } z|t)| �� t!�"d� W Y d }~�q%d }~w t*j+�y� } z
|j,j-}W Y d }~n&d }~w t.�y } z|}W Y d }~nd }~w   t/�0�  t	d%� Y �q%|�1| �}|t2|d&��}t|j3j4�}t	t
jtj d|� dt
jtj5 � d'|� t
j6� dt
jtj7 � d(|d � d)|� � � �q%t|d �t|�k�r�t	t
jtj d* � t	t
jtj  d+ � t� }|dk�r�t8�  �q%t9�  �q%d S ),Nz	sessions/zsome thing has changedzEnter the code: � zdata.csvzUTF-8)�encoding�,r   )Z	delimiterZlineterminatorr   Zsrnor$   �username�   �id�   �namer#   r   �2   �wr%   � zno username, moving to nextZDONEzPlease Wait...�   �   ZPrivacyRestrictedError�   ZALREADYr   z(Script Are In Progress So Please Wait...�<   �Z   zUnexpected Error)Zchannelz > Group Members z>> z >> z
Members Added Successfully !
zPress Enter To Exit):�to_groupr   Zparse_phone�pphoner   �api_id�api_hashZconnectZis_user_authorizedr   r   ZBRIGHTr   �REDZsend_code_requestZsign_in�inputZGREENZget_me�	last_nameZ
first_name�open�csvr   �next�int�append�list�writerZwriterow�	nextdeltar   �YELLOW�time�sleepr   Z	randranger	   r   r   r
   r   r   ZRPCError�	__class__�__name__�	Exception�	traceback�	print_excZ
get_entityr   Z	full_chatZparticipants_count�RESETZ	RESET_ALL�CYAN�autos�quit) Zchannel_usernameZphoneZclient�userZ
LegendNameZ
input_fileZusers�fZrows�row�hash_obj�
csv_reader�list_of_rows�
row_number�
col_numberZnumnextZ	startfromZ	nextstartZnumendZendtoZnextendZdfrD   �status�gZcwfe�e�dZchannel_connectZchannel_full_infoZcountt�statr    r    r!   rP   H   s�   


�����
,�
���
V

��rP   )HZtelethon.syncr   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   r   r   r   Ztelethon.errors.rpcerrorlistr   r	   r
   r   Ztelethon.tl.functions.channelsr   r   r   Ztelethonr   r   r   Zconfigparser�sysr   r?   r   rL   rG   r   Zcoloramar   r   r   r   rN   �nZLIGHTGREEN_EXZlgr;   r   ZWHITEr0   rO   r   rF   r   Zcolorsr"   r>   rU   rV   rC   rW   rX   rY   ZnumdelrA   ZdeltarE   Zread_obj�valuer9   �strr:   r8   ZConfigParserZconfig�readr7   ZSLEEP_TIME_2rP   r    r    r    r!   �<module>   sl    ��	

o