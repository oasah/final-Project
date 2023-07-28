import streamlit as st
qestions=['1. 요즘 슬픈기분인가요?','2. 미래가 불안정하다고 생각하나요?', '3. 자신이 실패자라고 생각되나요?', '4. 일상에 만족하지 못하나요?','5. 죄책감을 느낄 때가 있나요?','6. 매순간 벌을 받는 느낌이 드나요?','7. 자신에게 실망하거나 싫은 기분인가요?','8. 안좋은 일이 생기면 자신을 탓하는 편인가요?','9. 요즘 우는날이 많아지진 않았나요?','10. 최근에 짜증이 늘었나요?','11. 주위 또는 주변사람들에게 관심을 가지고 있지 않나요?','12. 결정을 쉽게 내리지 못하나요?','13. 자신의 외모에 만족하지 못하나요?','14. 일(공부등 개인이 수행하는 것) 을 시작할 때의 의지가 부족한가요?','15. 최근 수면 패턴이 불규칙한가요?','16. 최근 많이 피로하지 않나요?','17. 최근 식욕이 떨어지진 않았나요?','18. 최근에 심리적인 이유로 체중에 큰 변화가 있었나요?','19. 건강이 딱히 중요하지 않다고 생각하나요?','20. 최근 무기력하여 아무것도 하기싫은 감정이 들때가 있었나요?']
answer=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
select=['전혀 그렇지 않다','그렇지 않다','보통인 편이다','그렇다','매우 그렇다']

st.title('We take care of your Mind 👋')
st.markdown('당신의 **심리**를 관리해드립니다')
st.markdown('')
st.markdown('과거부터 현재까지 :blue[우울증]환자가 꾸준히 :green[증가]하고 있었다는 사실을 알고 계시나요?')
st.markdown('그 어느때보다 :blue[자기자신의 심리]에 집중하고 그에 따른 대처를 해야할 시기입니다 ❗')
st.markdown('심리테스트를 통해 자신의 심리상태를 확인하고 그에따른 솔루션을 제공받으세요 👌 ')

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.title('Take a Psychological Test 👌')
st.markdown('자, 그럼 **심리 테스트**를 진행해볼까요?')
st.warning('정답을 찾는 테스트가 아니니, 평소 자신의 행동과 감정을 바탕으로 솔직하게 답변해주세요 🔥')
st.markdown('')
st.markdown('')
st.markdown('')
counter=0
for i in range(20):
	answer[i]=st.selectbox(qestions[i],select)
	if answer[i]=='전혀 그렇지 않다':
		counter+=1
	elif answer[i]=='그렇지 않다':
		counter+=2
	elif answer[i]=='보통인 편이다':
		counter+=3
	elif answer[i]=='그렇다':
		counter+=4
	else:
		counter+=5

testanswer=0
st.info('심리테스트가 모두 끝났어요! 결과를 확인해보세요 😊')
N=counter
if N<=30:
	st.markdown("와우~! 축하해요! 당신은 우울증 지수에서 가장 낮은 **전혀 우울하지 않은 상태** 입니다! 삶을 즐기고 있으시군요 😎")
	testanswer='전혀 우울하지 않은 상태'
elif N<=40:
	st.markdown("긍정적으로 살아가시는군요~ 적당히 **살아가며 느낄수있는 일반적인 우울수치** 입니다! 심각한 상태가 아니니 전혀 걱정하지 않으셔도 됩니다 😊")
	testanswer='긍정적인 상태'
elif N<=60:
	st.markdown("당신은 **가벼운 우울 상태** 입니다. 혹시 조금씩 지쳐가는 요즘, 이정도는 별일 아니라며 그냥 지나치고 있나요? 행복한 당신의 삶을 위해 취미생활, 독서등 일상속의 휴식을 찾길바래요 👌")
	testanswer='가벼운 우울'
elif N<=80:
	st.markdown("진지한 해결 방안이 필요해요! 당신은 **상당히 우울한 상태**입니다. 지금 극복하지 못한다면 심각한 상태로 이어질수 있어요. 책읽기, 산책, 취미생활등의 일상적인 노력으로 극복해보아요! 혼자선 힘들다면 주변인들에게 도움을 요청할것을 권해요 💊")
	testanswer='조금 심각'
	st.error('우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족·지인이 있을 경우 자살예방상담 전화 ☎1393, 정신건강상담 전화 ☎1577-0199, 희망의 전화 ☎129, 생명의 전화 ☎1588-9191, 청소년 전화 ☎1388, 청소년 모바일 상담 ‘다 들어줄 개’ 어플, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.')
elif N<=100:
	st.markdown("❗ 누군가의 전문적인 도움이 필요해요! 당신은 우울증 지수에서 가장높은 단계에 속하는 **심각하게 우울한 상태**입니다. 책읽기, 산책등의 일상적인 노력으로는 극복하지 못했다면 심리상담으로 전문적인 도움을 받을것을 권해요 ❗")
	testanswer='많이 심각'
	st.error('우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족·지인이 있을 경우 자살예방상담 전화 ☎1393, 정신건강상담 전화 ☎1577-0199, 희망의 전화 ☎129, 생명의 전화 ☎1588-9191, 청소년 전화 ☎1388, 청소년 모바일 상담 ‘다 들어줄 개’ 어플, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.')

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.title('A prescription just for you 💊')
st.markdown('**심리테스트**를 통한 결과를 모두 확인 하셨나요?')
st.markdown('지금부터 심리테스트를 통해 받은 결과를 바탕으로 :green[당신만을 위한 심리 진단서]를 보여드릴게요 🙂')
st.markdown('아! 그전에 진단서 발급을 위한 간단한 조사를 진행할게요 ❗')
st.warning('성실하게 답변해주실수록 진단서의 정확도와 효과는 올라가요 🔥')
st.markdown('')
st.markdown('')
st.markdown('')
name = st.text_input('이름을 입력해주세요')
years=st.number_input('나이를 입력해주세요', 1, 100)

if testanswer=='전혀 우울하지 않은 상태':
	veryhappy = st.text_area(f"{name}님이 가장 행복할 때는 언제인가요?", height=3)
	happywords = st.text_area(f"{name}님이 들었을 때 가장 기분이 좋아지는 말은 무엇인가요?", height=3)
	sadwords = st.text_area(f"반대로 {name}님이 들었을 때 가장 기분이 안좋아지는 말은 무엇인가요?", height=3)
	hobby = st.text_area(f"{name}님의 취미가 있으신가요?", height=3)
	friend = st.text_area(f"{name}님의 가장 친한 친구를 1명 말해주세요!", height=3)
	tome = st.text_area(f"{name}님이 자기자신에게 해주고 싶은 말은 무엇인가요?", height=3)

	st.markdown('')
	st.markdown('')


	st.title(f'Check the diagnosis 🙂')
	st.markdown('**아래의 버튼**을 눌러 진단서를 확인해보세요!')
	veryhappyy=st.button('진단서 확인하기 💊')

	if veryhappyy:
		st.title(f'{name}의 님의 심리 진단서 💊')
		st.markdown(f'이름 : {name}')
		st.markdown(f'나이 : {years}')
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**종합의견**')
		st.markdown(f"심리테스트 결과 {name}님은 매우 행복한 상태로 진단되었어요 😊")
		st.markdown(f"{name}님이 행복하시다니, 저까지 행복해지는 느낌이 드네요 ❗😎")
		st.markdown(f"{name}님은 {veryhappy} 가장 행복하시고, {happywords}라는 말을 들을 때 좋아하시는군요!")
		st.markdown(f"저도 이 부분은 매우 공감해요 👌")
		st.markdown(f"하지만, 동전에서도 양면은 존재하듯이 {name}님도 {sadwords}라는 말을 들을 때처럼 기분이 안좋아질 때가 분명 있을거예요")
		st.markdown(f"그럴때는 {hobby}를 하시거나 {name}님의 가장 친한 친구인 {friend}님에게 고민을 털어놓아보세요 ❗")
		st.markdown(f"항상 {name}님의 앞날에 행복하고 웃을 수 있는 날만이 가득하기를 응원할게요 ❗ 화이팅 😊")
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**솔루션**')
		st.markdown(f'💊 자기자신에게 {tome}라고 말해주기')

if testanswer=='긍정적인 상태':
	hoppy = st.text_area(f"{name}님이 지금까지 살아오면서 가장 기뻤던 순간이 있나요?", height=3)
	sod = st.text_area(f"그렇다면 반대로 {name}님이 지금까지 살아오면서 가장 슬펐던 순간이 있나요?", height=3)
	people = st.text_area(f"{name}님이 생각하시기에 이 세상에서 가장 아름다운 것이 무엇이라고 생각하시나요?", height=3)
	habby = st.text_area(f"{name}님의 취미는 무엇인가요?", height=3)
	friendd = st.text_area(f"{name}님이 인생을 살아가면서 가장 의지하는 사람은 누구인가요?", height=3)
	model = st.text_area(f"{name}님의 롤모델이 있나요?", height=3)
	dream = st.text_area(f"{name}님의 꿈이 있나요?", height=3)
	toome = st.text_area(f"{name}님이 자기자신에게 해주고 싶은 말이 있나요?", height=3)
	st.markdown('')
	st.markdown('')


	st.title(f'Check the diagnosis 🙂')
	st.markdown('**아래의 버튼**을 눌러 진단서를 확인해보세요!')
	happyy=st.button('진단서 확인하기 💊')

	if happyy:
		st.title(f'{name}의 님의 심리 진단서 💊')
		st.markdown(f'이름 : {name}')
		st.markdown(f'나이 : {years}')
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**종합의견**')
		st.markdown(f"심리테스트 결과 {name}님은 긍정적인 상태로 진단되었어요 🙂")
		st.markdown(f"{name}님께서 평소에 느끼시는 우울감은 충분히 느낄 수 있는 우울감이예요!")
		st.markdown(f"하지만 {sod}와 같이 너무나도 큰 슬픔이 찾아오면 곧바로 넘어지기도 해요")
		st.markdown(f"그리고 그런 자기자신을 보면서 실망하기도 하고요")
		st.markdown(f"하지만 {name}님은 {people}보다도 더 아름다운 존재인것을 기억하시면 좋겠어요 ❗")
		st.markdown(f"가끔 {sod}와 같은 상황 속에서 넘어지더라도 다시 일어날 {name}님 자신을 믿으셨으면 좋겠어요 😊")
		st.markdown(f"평소에는 {habby}를 하거나 가끔 생기는 고민들을 {friendd}님에게 털어놓아보세요 ❗")
		st.markdown(f"그렇게 {dream}을 바라보면서 계속 넘어지고 깨지고 다시 일어서고를 반복하다보면")
		st.markdown(f"어느새 {name}님은 {model}님처럼, 혹은 그 너머로 성장해있을거예요 😊")
		st.markdown(f"{name}님의 인생에 항상 행복한 경험들이 가득 쌓이기를 바랄게요❗ 언제나 {name}님을 응원해요 ❗")
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**솔루션**')
		st.markdown(f'💊 자기자신에게 {toome}라고 말해주기')
		st.markdown(f'✔️ {dream}을 이룰 수 있는 방법 생각해보기')
		st.markdown(f'💊 성장일기 기록하기')
		st.markdown(f'✔️ {model}님에게서 배울 것들의 리스트를 정리하고 하나하나 실행시켜보기')

if testanswer=='가벼운 우울':
	saddy = st.text_area(f"최근 우울했던 경험이 있었나요?", height=3)
	besthappy = st.text_area(f"반대로 {name}님이 지금까지 살아오면서 가장 기뻤던 순간이 있나요?", height=3)
	favorite = st.text_area(f"{name}님에게 가장 소중한 존재는 누구인가요?", height=3)
	bucket = st.text_area(f"{name}님이 인생을 살아가면서 꼭 이루고자 하는 소원이 있나요?", height=3)
	myself = st.text_area(f"{name}님은 어떨때 자기자신을 보고 실망하나요?", height=3)
	again = st.text_area(f"{name}님은 어떨때 다시 일어날 힘을 얻으시나요?", height=3)
	food = st.text_area(f"{name}님이 가장 좋아하는 음식을 적어주세요")
	music = st.text_area(f"{name}님이 가장 좋아하는 음악을 적어주세요")
	dreaming = st.text_area(f"{name}님의 꿈이 있나요?", height=3)
	fromme = st.text_area(f"{name}님이 자기자신에게 해주고 싶은 말이 있나요?", height=3)
	st.markdown('')
	st.markdown('')


	st.title(f'Check the diagnosis 🙂')
	st.markdown('**아래의 버튼**을 눌러 진단서를 확인해보세요!')
	veryhappyy=st.button('진단서 확인하기 💊')

	if veryhappyy:
		st.title(f'{name}의 님의 심리 진단서 💊')
		st.markdown(f'이름 : {name}')
		st.markdown(f'나이 : {years}')
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**종합의견**')
		st.markdown(f"심리테스트 결과 {name}님은 가벼운 우울로 진단되었어요 🎈")
		st.markdown(f"{name}님께서는 우울감을 평균보다 살짝 더 많이 느끼시는 편이예요")
		st.markdown(f"그 이유는 저도 알 수 없지만, 아마 {saddy}와 같은 경험들이 모여 만들어낸 결과라고 생각해요")
		st.markdown(f"그리고 {name}님은 자기자신에게 {myself}와 같은 상황이 일어나면 실망을 하시는군요")
		st.markdown(f"이점에 대해서는 저도 많이 공감이 되는 것 같아요")
		st.markdown(f"하지만 정말 다행인것은 {name}님의 인생에 이미 {besthappy}와 같은 아름다운 상황이 존재했고,")
		st.markdown(f"계속해서 존재할것이라는 사실이예요 😊")
		st.markdown(f"그리고 {name}님에게는 {favorite}과 같은 좋은 사람들이 있고, {dreaming}이라는 멋진 꿈도 있네요 ❗")
		st.markdown(f"이미 모든 상황들이 {name}님께서는 좋은 사람이라는 것을 가리키고 있네요 😊")
		st.markdown(f"가끔, 혹은 자주 우울함과 좌절감이 {name}님을 덮을 수 있어요")
		st.markdown(f"그렇지만, 그러한 상황상황들 마다 {again} 같은 방법을 사용해서 헤쳐나갈 {name}님이라는 것을 기억하세요 ❗")
		st.markdown(f"그리고 우울한 상황이 찾아보면 {bucket}과 같은 {name}님의 버킷리스트도 생각해보기를 추천드려요 🙂")
		st.markdown(f"{name}님의 인생이라는 페이지에 아름다운 그림만이 가득하기를 바랄게요 😊")
		st.markdown(f"언젠가는 빛날, 그리고 이미 빛나고 있는 {name}님의 인생을 응원합니다 ❗")
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**솔루션**')
		st.markdown(f'💊 자기자신에게 {fromme}라고 말해주기')
		st.markdown(f'✔️ 버킷리스트 작성해보기')
		st.markdown(f'💊 우울한 기분이 들때마다 {food}를 먹거나 {music} 듣기')
		st.markdown(f'✔️ {name}님 옆에는 {favorite}과 같은 좋은 사람들이 있어요 ❗')
		st.markdown(f'💊 항상 {name}님은 멋진 사람이라는 것을 기억하기')


if testanswer=='조금 심각':
	a = st.text_area(f"인생에서 가장 행복했던 순간은 언제인가요?", height=3)
	b = st.text_area(f"{name}님이 생각하시기에 이 세상에서 가장 좋은 사람은 누구인것같나요?", height=3)
	d = st.text_area(f"{name}의 인생의 가장 최종적인 목표는 무엇인가요?", height=3)
	e = st.text_area(f"{name}님이 꼭 이루고 싶은 소원이 있나요?", height=3)
	f = st.text_area(f"{name}님이 가장 낙담하는 순간은 언제인가요?", height=3)
	g = st.text_area(f"{name}님이 사랑하는 존재가 있나요?")
	h = st.text_area(f"{name}님이 자기자신에게 실망할 때가 있나요?")
	i = st.text_area(f"{name}님의 꿈이 있나요?", height=3)
	j = st.text_area(f"{name}님이 자기자신에게 해주고 싶은 말이 있나요?", height=3)
	st.markdown('')
	st.markdown('')


	st.title(f'Check the diagnosis 🙂')
	st.markdown('**아래의 버튼**을 눌러 진단서를 확인해보세요!')
	veryhappyy=st.button('진단서 확인하기 💊')

	if veryhappyy:
		st.title(f'{name}의 님의 심리 진단서 💊')
		st.markdown(f'이름 : {name}')
		st.markdown(f'나이 : {years}')
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**종합의견**')
		st.markdown(f"심리테스트 결과 {name}님은 다소 심각한 우울로 진단되었어요 💊")
		st.markdown(f"{name}님께서는 항상 인생을 살아가시면서 정말 최선을 다하시는 분 같아요")
		st.markdown(f"하지만 그것만큼 잘 되지 않고 매일 실패하고 좌절하는 {name}님의 모습을 보면서 많이 실망하시는 것 같아요")
		st.markdown(f"특히 {h}와 같은 상황에서 잘 실망하시네요")
		st.markdown(f"하지만, 이점을 기억하시면 좋겠어요. {name}님은 {b}님처럼 너무나도 좋은 사람인것을요")
		st.markdown(f"지금은 잘 받아들여지지 않을 수 있어요. 그렇지만 {name}님께서는 {i}라는 꿈이 있는 멋진 사람인것 같아요 ❗")
		st.markdown(f"그리고 {d}라는 인생의 목표까지 존재한다니, 대단한데요 ? 😊")
		st.markdown(f"항상, 언제 어디서나 무조건 행복할 수는 없어요. 분명 {f}와 같은 {name}님을 넘어뜨리는 일들이 존재할거예요")
		st.markdown(f"하지만 이런 상황에서는 {e}와 {g}님과 같은 좋은 것들만 생각하면서 극복하는 힘을 길러야해요")
		st.markdown(f"{name}님은 {a}라는 아름다운 상황을 경험해본 아주아주 멋진 사람이예요!")
		st.markdown(f"울땐 울고 웃을 땐 웃으며 {name}님의 인생에 행복한 모습이 가득하면 좋겠어요")
		st.markdown(f"지금 {name}님의 상황이 끝없이 펼쳐진 터널같다고 해도 이러한 상황도 반드시 지나갈테니 너무 낙심하지 마세요 😊")
		st.markdown(f"{name}님의 인생에 아름다운 인연과 경험들이 가득하기를 간절히 기도할게요 🙏")
		st.markdown(f"항상 {name}님을 응원해요 ! 화이팅 ❗")
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**솔루션**')
		st.markdown(f'💊 자기자신에게 {j}라고 말해주기')
		st.markdown(f'✔️ 인생을 살아오면서 행복했던 일들 적어보기')
		st.markdown(f'💊 매일매일 감사노트 작성해보기')
		st.markdown(f'✔️ 우울감을 극복할 수 있는 나만의 솔루션 만들기')
		st.error('우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족·지인이 있을 경우 자살예방상담 전화 ☎1393, 정신건강상담 전화 ☎1577-0199, 희망의 전화 ☎129, 생명의 전화 ☎1588-9191, 청소년 전화 ☎1388, 청소년 모바일 상담 ‘다 들어줄 개’ 어플, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.')

if testanswer=='많이 심각':
	l = st.text_area(f"{name}님이 가장 행복했던 순간은 언제인가요?")
	m = st.text_area(f"{name}님이 인생을 살아가는 목적이 무엇인가요?", height=3)
	n = st.text_area(f"{name}님이 가장 소중하게 생각하는 존재들이 있나요?", height=3)
	o = st.text_area(f"{name}님을 항상 소중하게 여겨주는 존재들이 있나요?", height=3)
	p = st.text_area(f"{name}님은 어떨때 세상이 무너진듯한 느낌을 받나요?")
	q = st.text_area(f"{name}이 인생이 가치있다고 느껴질때는 언제인가요?")
	r = st.text_area(f"{name}님의 꿈이 있나요?", height=3)
	s = st.text_area(f"{name}님이 자기자신에게 해주고 싶은 말이 있나요?", height=3)
	st.markdown('')
	st.markdown('')


	st.title(f'Check the diagnosis 🙂')
	st.markdown('**아래의 버튼**을 눌러 진단서를 확인해보세요!')
	veryhappyy=st.button('진단서 확인하기 💊')

	if veryhappyy:
		st.title(f'{name}의 님의 심리 진단서 💊')
		st.markdown(f'이름 : {name}')
		st.markdown(f'나이 : {years}')
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**종합의견**')
		st.markdown(f"심리테스트 결과 {name}님은 매우 심각한 우울로 진단되었어요 💊")
		st.markdown(f"{name}님께서는 죽고싶다는 생각과 인생을 포기하고 싶다는 생각을 자주 하시는것 같아요")
		st.markdown(f"그만큼 {name}님께서 인생을 최선을 다해 살았고, 열정적으로 살아냈다는 뜻이겠죠?")
		st.markdown(f"하지만, 인생에서 쉬어가야 할 타이밍을 놓치신 것 같아요")
		st.markdown(f"안대를 쓴 경주마처럼 앞만보고 뛰어가느라 정작 {m}과 같은 인생의 목적은 새까맣게 까먹고 있었을거예요")
		st.markdown(f"그리고 {p}와 같은 상황에서도 실패한것을 모두 '자기자신의 탓'으로 돌리시는 것 같아요")
		st.markdown(f"지금 저는 {name}님의 짐의 무게를 예측조차 할 수 없을 것 같아요")
		st.markdown(f"어떤것이 {name}님을 힘들게 했던지, 그것이 공부이든 친구들이든 가족이든 혹은 {name}님 자신이든,")
		st.markdown(f"그렇게 {name}님을 힘들게 하는 모든 요소들을 점검해보고 해결해 나가야 할 때인 것 같아요")
		st.markdown(f"울땐 울고 웃을 땐 웃으며 {name}님의 인생에 행복한 모습이 가득하면 좋겠어요")
		st.markdown(f"쉽게 {name}님의 인생을 포기해버리지 않았으면 좋겠어요")
		st.markdown(f"{name}님이 {n}님들을 소중히 생각하는 만큼, {o}님들과 모든 사람들이 {name}님을 소중하게 생각해요")
		st.markdown(f"그렇기에 {name}님, 우리 조금만 더 힘을 내보는 것 어떨까요? 💊")
		st.markdown(f"제가, 그리고 모든 사람들이 {name}님의 {r}라는 꿈을 응원해요 ❗")
		st.markdown(f"{name}님의 마음속에 더이상 깊은 상처들이 생기지 않기를, 그리고 이미 있었다면")
		st.markdown(f"그 상처들이 계속해서 나아지기를 간절히 바라겠습니다 🙏")
		st.markdown('')
		st.markdown('----------------------------------------------------------------------------------------------')
		st.markdown('')
		st.markdown('**솔루션**')
		st.markdown(f'💊 자기자신에게 {s}라고 말해주기')
		st.markdown(f'✔️ 우울증 관련 전문가 상담 받아보기')
		st.markdown(f'💊 소중한 사람들과 많은 시간 보내기 - 혼자 있는 시간 줄이기')
		st.markdown(f'✔️ {name}님은 그 누구보다도 빛나고 아름답다는 것을 기억하기')
		st.error('우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족·지인이 있을 경우 자살예방상담 전화 ☎1393, 정신건강상담 전화 ☎1577-0199, 희망의 전화 ☎129, 생명의 전화 ☎1588-9191, 청소년 전화 ☎1388, 청소년 모바일 상담 ‘다 들어줄 개’ 어플, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.')

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.title('Tips 🌟')
st.markdown('**당신만을 위한 심리 진단서**를 모두 진단받으셨나요?')
st.markdown('아래에서 :blue[심리를 관리하기 위한 다양한 팁]들을 확인하실 수 있답니다 ❗')
st.markdown('Tips에서 이룬 목표들은 체크를 하여 목표에 도달한것을 표시해보세요 😊')
st.markdown('')
st.markdown('')
st.info('**행복한 삶**을 사는 태도 📌')

firstlist=['1. 기분이 태도가 되지 않기 😄','2. 나만 힘든 관계는 정리하기 ❗','3. 말하는 중에 끊지 않기 😗','4. 행복은 사소한 것에서 온다는 것 기억하기 💙','5. 기대만큼이나 나를 쉽게 망치는 것 없음을 기억하기 🥲','6. 말해야 할지 말아야 할지 고민된다면 말하지 않기 🙏','7. 한 번 아닌 건 영원히 아니라는 것을 기억하기 🙅‍','8. 애써 모두에게 좋은 사람이 될 필요는 없음을 기억하기 😎','9. 나의 가치를 의심하지 말자. 내가 가장 소중한 사람이다 🌟']
firstcheck=[]

one=st.checkbox(firstlist[0])
if one:
	firstcheck.append(firstlist[0])

second=st.checkbox(firstlist[1])
if second:
	firstcheck.append(firstlist[1])

third=st.checkbox(firstlist[2])
if third:
	firstcheck.append(firstlist[2])
fourth=st.checkbox(firstlist[3])
if fourth:
	firstcheck.append(firstlist[3])
fifth=st.checkbox(firstlist[4])
if fifth:
	firstcheck.append(firstlist[4])
sixth=st.checkbox(firstlist[5])
if sixth:
	firstcheck.append(firstlist[5])
seventh=st.checkbox(firstlist[6])
if seventh:
	firstcheck.append(firstlist[6])
eighth=st.checkbox(firstlist[7])
if eighth:
	firstcheck.append(firstlist[7])
ninth=st.checkbox(firstlist[8])
if ninth:
	firstcheck.append(firstlist[8])

st.markdown('')
st.markdown('')

st.info('**우울을 극복**할 수 있는 다양한 방법들 🌟')

secondcheck=[]
ai=st.checkbox('노래듣기 🎵 : 위로되는 노래나 신나는 노래를 들으면 우울을 극복할 수 있지 않을까요?')
if ai:
	secondcheck.append(ai)

bi=st.checkbox('감사일기 작성하기 📖 : 매일 감사한일을 기록하다 보면 저절로 행복해질거예요!')
if bi:
	secondcheck.append(bi)
ci=st.checkbox('일찍 일어나기 ☀️ : 일찍일어나는 좋은 습관을 가져보세요 !')
if ci:
	secondcheck.append(ci)
di=st.checkbox('재밌는 영상보기 😂 : 웃긴 예능이나 영상을 보면서 크게 웃다보면 행복해진답니다!')
if di:
	secondcheck.append(di)
ei=st.checkbox('버킷리스트 작성하기 🎈 : 인생을 살아가면서 이루고 싶은 소망들을 정리하면 이것이 어느새 자신의 원동력이 되어 있답니다!')
if ei:
	secondcheck.append(ei)
fi=st.checkbox('매일 좋은 글귀 읽기 ❤️ : 매일매일 응원이 되는 글귀를 읽다보면 아마 자기자신의 마인드도 그렇게 변화되어 있을거예요!')
if fi:
	secondcheck.append(fi)
gi=st.checkbox('운동 시작하기 ⚽ : 운동을 시작하여 끈기와 지구력을 길러보세요 !')
if gi:
	secondcheck.append(gi)
hi=st.checkbox('친구들과 같이 시간보내기 💕 : 친구들과 같은 소중한 이들과 시간을 보내다보면 저절로 행복해진답니다!')
if hi:
	secondcheck.append(hi)
ii=st.checkbox('인생의 목표와 꿈 정하기 ✔️ : 인생을 살아가면서 이룰 목표와 꿈을 세운다면 더욱 보람찬 삶을 살아갈 수 있겠죠?')
if ii:
	secondcheck.append(ii)

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.title('Final 👏')
st.markdown('지금까지 여러가지 질문들을 통해 심리를 관리해드렸습니다 😊')
st.markdown(f'검사는 모두 끝났지만 위의 Tips를 활용하여 목표달성을 꾸준히 하는 {name}님의 개인적인 노력도 반드시 필요해요 ❗')
st.markdown('TIps의 목표달성을 통해 심리를 관리해보는 것을 추천드립니다 😊')
st.markdown(f"{name}님은 너무나도 대단하고 멋진 사람이기 때문에 반드시 해낼 수 있을거라고 생각되는데요 ❗")
st.markdown(f"{name}님의 앞으로의 수많은 날들과 도전들을 항상 응원합니다 ❗💕")
