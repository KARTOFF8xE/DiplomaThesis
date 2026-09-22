FROM ubuntu:noble

ENV DEBIAN_FRONTEND=noninteractive

### TeX
RUN set -x && \
  apt update -y -qq && \
  apt install -y -qq \
    texlive-full \
    sudo \
    wget curl zip unzip tar \
    nano \
    git && \
  apt-get autoremove -y -qq

### User
ARG USERNAME=user
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

### Create the user
# RUN groupadd --gid $USER_GID $USERNAME
# RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

### zsh
RUN apt install wget zsh curl rustc cargo -y
RUN git clone https://github.com/ogham/exa.git && \
  cd exa && \
  cargo build --release && \
  cp target/release/exa /usr/local/bin/
RUN wget https://raw.githubusercontent.com/KARTOFF8xE/configs/main/zsh/.zshrc -O /home/$USERNAME/.zshrc
RUN wget "https://github.com/sharkdp/vivid/releases/download/v0.8.0/vivid_0.8.0_amd64.deb" -O /tmp/vivid && \
  dpkg -i /tmp/vivid
RUN mkdir -p /home/$USERNAME/.zsh_scripts && \
  git clone https://github.com/jimmijj/chromatic-zsh.git /home/$USERNAME/.zsh_scripts/chromatic-zsh
RUN mkdir -p /home/$USERNAME/.zsh_scripts/plugins && \
  git clone https://github.com/zsh-users/zsh-autosuggestions.git /home/$USERNAME/.zsh_scripts/plugins/zsh-autosuggestions && \
  wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/git/git.plugin.zsh -O /home/$USERNAME/.zsh_scripts/plugins/git.plugin.zsh && \
  zsh -c "source /home/$USERNAME/.zsh_scripts/plugins/git.plugin.zsh"
RUN mkdir -p /home/$USERNAME/.cache/zsh && \
  touch /home/$USERNAME/.cache/zsh/history
RUN SNIPPET="export HISTFILE=/home/$USERNAME/.cache/zsh/history \nsetopt APPEND_HISTORY \nsetopt INC_APPEND_HISTORY \nsetopt SHARE_HISTORY\n" \
  && echo "$SNIPPET" >> "/home/$USERNAME/.zshrc"
RUN chmod 777 /home/$USERNAME/.cache/zsh
RUN chsh $user -s $(which zsh)

### Add sudo support
RUN set -x && \
  echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
  chmod 0440 /etc/sudoers.d/$USERNAME

### Set the home directory and user
WORKDIR /home/${USERNAME}
USER $USERNAME

COPY --chown=${USERNAME}:${USERNAME} tubaf-3.0.1.zip /tmp/tubaf-latex.zip
RUN set -x && \
  mkdir -p texmf/tex/latex/ && \
  unzip /tmp/tubaf-latex.zip -d texmf/tex/latex/

RUN set -x && \
  echo "alias x='exit'" >> ~/.bash_aliases && \
  echo "alias c='clear'" >> ~/.bash_aliases

RUN ln -s build/main.pdf main.pdf
CMD [ "bash" ]